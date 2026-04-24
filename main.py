from fastapi import FastAPI

from api.routes.crianca import router as crianca_router
from api.routes.brinquedo import router as brinquedo_router
from api.routes.emprestimo import router as emprestimo_router

app = FastAPI()

app.include_router(crianca_router)
app.include_router(brinquedo_router)
app.include_router(emprestimo_router)