from x1banco import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Text,Boolean,DateTime, CheckConstraint,Float
from sqlalchemy.orm import relationship
import datetime

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key = True,index = True)
    email = Column(String, unique=True, index = True)
    compras = relationship("Pedido",backref="usuario")
class Curso(Base):
    __tablename__ = "cursos"
    __table_args__ = (CheckConstraint("vagas_disponiveis >= 0"),)
    id = Column(Integer,primary_key=True,index=True)
    titulo = Column(String,index=True,nullable=False)
    preco = Column(Float,index=True,nullable=False)
    vagas_disponiveis = Column(Integer,index=True,nullable=False)
    caminho_video = Column(String,nullable=False)
class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer,primary_key=True,index=False)
    usuario_id = Column(Integer,ForeignKey("usuarios.id"))
    curso_id = Column(Integer,ForeignKey("cursos.id"))
    pago = Column(Boolean,default= False, nullable=False,index=True)

