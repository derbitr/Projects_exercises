from fastapi import APIRouter,FastAPI,HTTPException,Depends
import a1classes,a4basedadosclasses
from a3basedados import Sessao_local
from sqlalchemy.orm import Session

roteador = APIRouter()

def banco_local():
    banco = Sessao_local()
    try:
        yield banco
    finally:
        banco.close()

@roteador.post("/tarefas")
async def postar_tarefas(nova_tarefa : a1classes.Tarefa,db: Session = Depends(banco_local)):
    tarefa_banco = a4basedadosclasses.Tarefadb(
        titulo = nova_tarefa.titulo,
        descricao = nova_tarefa.descricao,
        concluida = nova_tarefa.conclusao
    )
    db.add(tarefa_banco)
    db.commit()
    db.refresh(tarefa_banco)
    return {"mensagem": "Sucesso", "tarefa": tarefa_banco}

@roteador.get("/tarefas")
async def pegar_tarefas(db : Session = Depends(banco_local)):
    tarefas = db.query(a4basedadosclasses.Tarefadb).all()
    return tarefas
@roteador.put("/tarefas/{tarefa_id}")
async def colocar_tarefas(tarefa_id:int,tarefa_atualizada : a1classes.Tarefa,db : Session = Depends(banco_local)):
    tarefa_existente = db.query(a4basedadosclasses.Tarefadb).filter(a4basedadosclasses.Tarefadb.id ==tarefa_id).first()
    if not tarefa_existente:
        raise HTTPException(status_code=404,detail="Tarefa não encontrada")
    tarefa_existente.titulo = tarefa_atualizada.titulo
    tarefa_existente.descricao = tarefa_atualizada.descricao
    tarefa_existente.concluida = tarefa_atualizada.conclusao
    db.commit()
    db.refresh(tarefa_existente)
    return {"mensagem": "Tarefa atualizada", "tarefa": tarefa_existente}
@roteador.delete("/tarefas/{tarefa_id}")
async def deletar_tarefas(tarefa_id : int, db: Session = Depends(banco_local)):
    tarefa_deletar = db.query(a4basedadosclasses.Tarefadb).filter(a4basedadosclasses.Tarefadb.id == tarefa_id).first()
    if not tarefa_deletar:
        raise HTTPException(status_code=404,detail="Tarefa não encontrada")
    db.delete(tarefa_deletar)
    db.commit()
    return {"mensagem": "tarefa removida"}