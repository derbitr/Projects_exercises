import c1banco, psycopg2,c2modelos
from sqlalchemy.orm import Session
from fastapi import HTTPException

def banco_local():
    banco = c1banco.Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
def transacoes(pedido : c2modelos.ItemPedido, db : Session):
    try:
        produto = db.query(c2modelos.Produto).filter(c2modelos.Produto.id == pedido.produto_id).with_for_update().first()
        if produto.estoque < pedido.quantidade:
            raise HTTPException(status_code=500,detail="Estoque unsuficiente")
        else:
            pedido.preco_produto = produto.preco
            produto.estoque -= pedido.quantidade
        return produto
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=401, detail=str(e))
def confirmar_venda(id_pedido: int, db : Session):
    try:
        pedido = db.query(c2modelos.Pedido).filter(c2modelos.Pedido.id == id_pedido)
        if not pedido:
            raise Exception("Pedido não encontrado")
        if pedido:
            return pedido
        for item in pedido.itens:
            transacoes(item,db)
        pedido.status = True
        return pedido
    except Exception as g:
        raise Exception(g)