from typing import Dict
from domain.crianca import Crianca
from domain.brinquedo import Brinquedo
from domain.emprestimo import Emprestimo

class MemoryDB:
    def __init__(self):
        self.crianca_por_nome: Dict[str, Crianca] = {}
        self.brinquedo_por_id: Dict[int, Brinquedo] = {}
        self.pedidos_por_codigo: Dict[int, Pedido] = {}

db = MemoryDB()