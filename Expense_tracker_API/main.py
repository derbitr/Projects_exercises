from fastapi import FastAPI
import uvicorn

from core.logs import iniciar_log
from api.rotas_auth import roteador as rota_auth
from api.rotas_expenses import roteador_pendencias as rota_despesa

logger = iniciar_log("Registro")

app = FastAPI(
    title="Tracker API",
    description = "Sistema de monitoramento de despesas",
    version = "1.0"
)

app.include_router(rota_auth)
app.include_router(rota_despesa)
logger.info("Rotas iniciadas")


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8005)