from c1banco import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Text,Boolean,DateTime, CheckConstraint
from sqlalchemy.orm import relationship
import datetime

class Produto(Base):
    __tablename__ = "produtos"
    __table_args__ = (CheckConstraint('estoque >= 0', name="check_estoque_positivo"),) 
    id = Column(Integer,primary_key = True, index= True)
    nome = Column(String,index=True,nullable=False)
    preco = Column(Integer,index=True,nullable=False)
    estoque = Column(Integer,index=True)
class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer,primary_key=True,index=True)
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Boolean,nullable=False,default=False)
    itens = relationship("ItemPedido",backref="pedido")
class ItemPedido(Base):
    __tablename__ = "items"
    id = Column(Integer,primary_key=True,index=True)
    pedido_id = Column(Integer,ForeignKey("pedidos.id"))
    produto_id = Column(Integer,ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    preco_produto = Column(Integer,nullable=False)
