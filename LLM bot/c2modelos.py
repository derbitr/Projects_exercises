from c1banco import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean,DateTime
from sqlalchemy.orm import relationship
import datetime

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    senha_hash = Column(String,nullable=False)
    tarefas = relationship("Tarefa",back_populates="dono")
    historico = relationship("MensagemChat",back_populates="usuario")
class Tarefa(Base):
    __tablename__ = 'tarefas'
    id = Column(Integer,primary_key=True,index=True)
    titulo = Column(String,nullable=False)
    dono_id = Column(Integer,ForeignKey("usuarios.id"),index=True)
    dono = relationship("Usuario",back_populates="tarefas")
class MensagemChat(Base):
    __tablename__ = 'mensagens'
    id = Column(Integer,primary_key=True,index=True)
    usuario_id = Column(Integer,ForeignKey("usuarios.id"))
    papel = Column(String,nullable=False)
    conteudo = Column(Text,nullable=False)
    criado_em = Column(DateTime,default=datetime.datetime.utcnow)
    usuario = relationship("Usuario",back_populates="historico")
