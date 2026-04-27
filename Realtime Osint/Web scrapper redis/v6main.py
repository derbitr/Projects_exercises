from fastapi import FastAPI
import uvicorn
from v4rotas import roteador

app = FastAPI(
    title="Scrapper com redis",
    description="Tarefas assincronas com redis para otimização de memória",
    version=0.5
)
app.include_router(roteador)

@app.get("/")
def ler_roteador():
    return {"Mensagem": "Sistema de bot scrap com otimização de memória", "docs" : "/docs"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)