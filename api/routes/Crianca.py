from fastapi import APIRouter, HTTPException
from schemas.crianca import CriancaCreate, CriancaOut
from services.emprestimo_service import service

router = APIRouter(prefix="/crianca", tags=["crianca"])

@router.post("", response_model=criancaOut)
def criar(payload: criancaCreate):
    try:
        cliente = service.criar_crianca(payload.id, payload.nome)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return CriancaOut(cpf=crianca.id, nome=crianca.nome)

@router.get("/{id}", response_model=criancaOut)
def obter(id: str):
    crianca = service.obter_crianca(id)
    if not crianca:
        raise HTTPException(
            status_code=404, 
            detail="crianca não encontrado"
            )
    return CriancaOut(id=crianca.id, nome=crianca.nome)