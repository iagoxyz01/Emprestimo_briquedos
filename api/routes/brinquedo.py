from fastapi import APIRouter
from repositories.memory import db
from domain.brinquedo import Brinquedo

router = APIRouter(prefix="/brinquedos")

@router.post("")
def criar(brinquedo: Brinquedo):
    db.brinquedos.append(brinquedo)
    return brinquedo

@router.get("")
def listar():
    return db.brinquedos