from fastapi import FastAPI
import c1banco
from c4financeiro import roteador
import uvicorn

app = FastAPI(
    title="Projeto teste ecommerce",
    description="Nao sei oq por aqui",
    version="1.0"
)
c1banco.Base.metadata.create_all(bind = c1banco.motor)

app.include_router(roteador)

@app.get("/")
def iniciar():
    return {"status": "Tá funcionando, eu acho"}

if __name__ == "__main__":
    iniciar()
    uvicorn.run(app,host="127.0.0.1",port=8005)
