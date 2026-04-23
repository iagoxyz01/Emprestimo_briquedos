from fastapi import APIRouter, HTTPException
from schemas.brinquedo import BrinquedoCreate, BrinquedoOut
from services.emprestimo_service import service

router = APIRouter(prefix="/brinquedo", tags=["briquedos"])


@router.post("", response_model=BrinquedoOut)
def criar(payload: BrinquedoCreate):
    produto = service.criar_brinquedo(
        payload.id,
        payload.nome,
        payload.categoria,
        payload.faixa_etaria_minima,
        payload.disponivel
    )
    return BrinquedoOut(**Brinquedo.__dict__)


@router.get("/{codigo}", response_model=BrinquedoOut)
def obter(codigo: int):
    brinquedo = service.obter_brinquedo(codigo)
    if not briquedos:
        raise HTTPException(status_code=404, detail="briquedo não encontrado")
    return BrinquedoOut(**briquedo.__dict__)

