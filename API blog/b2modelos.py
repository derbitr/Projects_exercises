from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from b1database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    senha_hash = Column(String,nullable=False)
    posts = relationship("Post",back_populates="autor")
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,index=True)
    titulo = Column(String,nullable=False)
    conteudo = Column(String,nullable=False)
    publicado = Column(Boolean, default=True)

    autor_id= Column(Integer,ForeignKey("usuarios.id"))
    autor = relationship("Usuario",back_populates="posts")