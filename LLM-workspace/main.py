import v1banco,v2modelos,v3moldes,v4jwt,v5ia,v6rotas,logging,uvicorn
from fastapi import FastAPI
from v6rotas import roteador

def configurar_banco():
    try:
        logging.info("Iniciando banco de dados")
        v2modelos.Base.metadata.create_all(bind = v1banco.motor)
    except Exception as e:
        logging.error(F"Ocorreu um erro: {e}")
def config():
    logging.basicConfig(level=logging.INFO, format = "%(levelname)s : %(message)s")
app = FastAPI(
    title= "Robozinho 2.0 agora vai (talvez)",
    description="É o mesmo mas pra fixar alguns conceitos na memoria muscular", #Exatamente isso lol #
    version= "1.0"  
                    )
app.include_router(roteador)
@app.get("/")
async def iniciar():
    return {"status": "online", "Projeto": "Assistente IA"}
if __name__ == "__main__":
    config()
    configurar_banco()
    logging.info("Iniciando servidor")
    uvicorn.run(app,host="127.0.0.1",port=8004)