from fastapi import APIRouter
from repositories.memory import db
from domain.crianca import Crianca

router = APIRouter(prefix="/criancas")

@router.post("")
def criar(crianca: Crianca):
    db.criancas.append(crianca)
    return crianca

@router.get("")
def listar():
    return db.criancas