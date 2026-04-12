from a2rotas import roteador
from fastapi import FastAPI
import logging,uvicorn
def config():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s : %(message)s")
app = FastAPI(
    title="Leve teste",
    description="Mesma coisinha mas com outras coisinhas",
    version="1.0"
)
app.include_router(roteador)
@app.get("/")
async def iniciar():
    return {"status": "online", "Projeto" : "Servidor de mídia"}
if __name__ == "__main__":
    config()
    logging.info("Iniciando")
    uvicorn.run(app,host="127.0.0.1",port=8006)