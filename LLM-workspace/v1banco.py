from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_ATUAL = os.path.join(DIRETORIO_ATUAL,"llmbot_banco.db")
os.path.exists(PASTA_ATUAL)
URL_BANCO = f"sqlite:///{PASTA_ATUAL}"
motor = create_engine(URL_BANCO, connect_args = {"check_same_thread": False})
Sessao_local = sessionmaker(autocommit = False,autoflush=False,bind=motor)
Base = declarative_base()
