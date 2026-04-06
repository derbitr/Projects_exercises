import c1banco,c2modelos,c3moldes,c4jwt,c5IA,c6rotas,logging,uvicorn
from fastapi import FastAPI
from c6rotas import roteador

def configurar_banco():
    try:
        logging.info("Iniciando banco de dados")
        c2modelos.Base.metadata.create_all(bind = c1banco.motor)
    except Exception as e:
        logging.error(F"Ocorreu um error ao acessar banco de dados {e}")
def config():
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")
app = FastAPI(
    title="Robozinho de teste ai calika",
    description="Sistema com banco de dados, JWT e integração Groq",
    version= "1.0"
)
app.include_router(roteador)
@app.get("/")
async def iniciar():
    return {"status":"Online","Projeto": "Assistente IA"}
if __name__ == "__main__":
    config()
    configurar_banco()
    logging.info("Iniciando servidor no port 8003")
    uvicorn.run(app,host="127.0.0.1",port=8003)
    