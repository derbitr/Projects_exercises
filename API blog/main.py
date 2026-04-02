from fastapi import FastAPI
import uvicorn
from b1database import motor, Base
import b5auth,b6authsemlogin,logging, b6authsemlogin

def config():
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s ")
def iniciar_banco_dados():
    try:
        logging.info("Iniciando banco de dados")
        Base.metadata.create_all(bind= motor)
    except Exception as e:
        logging.error(F"Falha ao iniciar o banco de dados: {e}")
app=FastAPI(title="Blog API",version="1.0")
app.include_router(b5auth.roteador, tags= ["Usuários e login"])
app.include_router(b6authsemlogin.roteador, tags= ["Posts do Blog"])
if __name__ =="__main__":
    config()
    iniciar_banco_dados()
    uvicorn.run(app,host="127.0.0.1",port=8003)