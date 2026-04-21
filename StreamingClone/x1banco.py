from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("BASE_URL")


DIRETORIO_ATUAL =os.path.dirname(os.path.abspath(__file__))
PASTA_ATUAL = os.path.join(DIRETORIO_ATUAL,"streaming.db")
os.path.exists()
URL_BANCO =f"{url}"
motor = create_engine(URL_BANCO)
Sessao_local = sessionmaker(autocommit = False, autoflush= False, bind=motor)
Base = declarative_base()

def get_db():
    banco = Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
