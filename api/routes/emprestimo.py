from fastapi import APIRouter
from services.emprestimo_service import EmprestimoService
from repositories.memory import db

router = APIRouter(prefix="/emprestimos")
service = EmprestimoService()

@router.post("")
def criar(crianca_id: int, brinquedo_id: int):
    return service.criar_emprestimo(crianca_id, brinquedo_id)

@router.get("")
def listar():
    return db.emprestimos

@router.get("/{id}")
def buscar(id: int):
    return next(e for e in db.emprestimos if e.id == id)

@router.put("/{id}/devolver")
def devolver(id: int):
    return service.devolver(id)

@router.get("/crianca/{id}")
def por_crianca(id: int):
    return [e for e in db.emprestimos if e.crianca_id == id]