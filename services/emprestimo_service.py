from datetime import datetime
from repositories.memory import db
from domain.emprestimo import Emprestimo

class EmprestimoService:

    def criar_emprestimo(self, crianca_id: int, brinquedo_id: int):
        crianca = next((c for c in db.criancas if c.id == crianca_id), None)
        brinquedo = next((b for b in db.brinquedos if b.id == brinquedo_id), None)

        if not crianca or not brinquedo:
            raise Exception("Crianca ou brinquedo não encontrado")

        if crianca.bloqueada:
            raise Exception("Crianca bloqueada")

        if not brinquedo.disponivel:
            raise Exception("Brinquedo indisponível")

        if crianca.idade < brinquedo.faixa_etaria_minima:
            raise Exception("Idade incompatível")

        emprestimos_ativos = [
            e for e in db.emprestimos
            if e.crianca_id == crianca_id and e.status == "ativo"
        ]

        if len(emprestimos_ativos) >= 2:
            raise Exception("Limite de empréstimos atingido")

        novo = Emprestimo(
            id=len(db.emprestimos) + 1,
            crianca_id=crianca_id,
            brinquedo_id=brinquedo_id,
            data_emprestimo=datetime.now()
        )

        brinquedo.disponivel = False
        db.emprestimos.append(novo)

        return novo

    def devolver(self, emprestimo_id: int):
        emprestimo = next((e for e in db.emprestimos if e.id == emprestimo_id), None)

        if not emprestimo:
            raise Exception("Emprestimo não encontrado")

        emprestimo.data_devolucao = datetime.now()
        emprestimo.status = "finalizado"

        dias = (emprestimo.data_devolucao - emprestimo.data_emprestimo).days

        if dias > 0:
            emprestimo.multa = dias * 2

        brinquedo = next((b for b in db.brinquedos if b.id == emprestimo.brinquedo_id), None)
        if brinquedo:
            brinquedo.disponivel = True

        atrasos = [
            e for e in db.emprestimos
            if e.crianca_id == emprestimo.crianca_id and e.multa > 0
        ]

        if len(atrasos) >= 3:
            crianca = next((c for c in db.criancas if c.id == emprestimo.crianca_id), None)
            if crianca:
                crianca.bloqueada = True

        return emprestimo