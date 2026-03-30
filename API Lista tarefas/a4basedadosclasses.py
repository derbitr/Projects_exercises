from sqlalchemy import Column, Integer, String, Boolean
from a3basedados import Base

class Tarefadb(Base):
    __tablename__ = "tabela_tarefas"
    id = Column(Integer,primary_key = True, index = True)
    titulo = Column(String, index = True)
    descricao = Column(String,nullable=True)
    concluida = Column(Boolean, default=False)
    