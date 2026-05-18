from fastapi import APIRouter, Depends, HTTPException
from core.logs import registro

roteador = APIRouter(prefix ="/api")
logger = registro("ROTEADOR_HTTP")


@roteador.get("/status",tags=["status"])
async def ler_mensagens():
    logger.info("Endpoint iniciado")
    return [{"status":"online"}]
@roteador.get("/mensagem/me",tags=["cliente"])
async def mensagem_cliente():
    return [{"mensagem": "HTTP conectado"}]
@roteador.get("/cliente",tags=["cliente"])
async def mensagem(cliente : str):
    if not cliente:
        raise HTTPException(
            status_code=403,detail="Nome inválido"
        )
    return {"cliente" : cliente}