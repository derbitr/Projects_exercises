import x1banco,psycopg2,x2modelos
from sqlalchemy.orm import Session
from fastapi import HTTPException


def transações(pedido : int, db : Session):
    try:
        pedido_db = db.query(x2modelos.Pedido).filter(x2modelos.Pedido.id == pedido.id).first()
        if not pedido_db:
            raise HTTPException(status_code=500,detail="Falha ao buscar")
        curso = db.query(x2modelos.Curso).filter(x2modelos.Curso.id== pedido.curso_id).with_for_update().first()
        if curso.vagas_disponiveis <=0:
            db.rollback()
            return False
        else:
            curso.vagas_disponiveis -= 1
            pedido_db.pago = True
            db.commit()
            return True
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=str(e))

