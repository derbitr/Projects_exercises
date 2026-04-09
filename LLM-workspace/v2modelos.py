from v1banco import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Text,Boolean,DateTime
from sqlalchemy.orm import relationship
import datetime

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    senha_hash = Column(String,nullable=False)
    tarefas = relationship("Tarefa",back_populates="dono")
    historico = relationship("MensagemChatBot",back_populates="usuario")
class Tarefa(Base):
    __tablename__ = 'tarefas'
    id = Column(Integer,primary_key=True,index=True)
    titulo = Column(String,nullable=False)
    concluido = Column(Boolean,nullable=False,default=False)
    dono_id = Column(Integer,ForeignKey("usuarios.id"),index=True)
    dono = relationship("Usuario",back_populates="tarefas")
class MensagemChatBot(Base):
    __tablename__ = 'mensagens'
    id = Column(Integer,primary_key=True,index=True)
    papel = Column(String,nullable=False)
    conteudo = Column(Text,nullable=False)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)
    dono_id = Column(Integer,ForeignKey("usuarios.id"),index=True)
    usuario = relationship("Usuario",back_populates="historico")
