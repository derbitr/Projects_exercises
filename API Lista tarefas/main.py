from fastapi import FastAPI
import a1classes,a2tarefas,uvicorn,logging
from a3basedados import motor,Base
import a4basedadosclasses

api = FastAPI(title="Api de tarefas",version="1.0")
def config():
    logging.basicConfig(level=logging.INFO,format= "%(levelname)s : %(message)s")
def ligar():
    api.include_router(a2tarefas.roteador)
Base.metadata.create_all(bind=motor)
if __name__ == "__main__":
    config()
    logging.info("Iniciando")
    ligar()
    uvicorn.run(api,host="127.0.0.1",port=8003)