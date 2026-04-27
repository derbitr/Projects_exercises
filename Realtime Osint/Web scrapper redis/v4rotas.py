from v1redis import app
from v3worker import dados
import v2modelos,requests,os
from fastapi import FastAPI, Request, HTTPException, APIRouter,Depends
from celery.result import AsyncResult

roteador = APIRouter(prefix="/Redis",tags=["Fila"])

@roteador.post("/extrair")
async def extracao(objeto : list[v2modelos.ScrapperAlvo]):
    lista_ids = []
    try:
        for item in objeto:
            tarefa = dados.delay(item)
            lista_ids.append(tarefa.id)
        return {"Status": "Processado", "ListaIds": lista_ids}
    except Exception as f:
        raise HTTPException(status_code=500,detail=str(f))
@roteador.get("/status/{task_id}")
async def consulta(task_id : str):
    try:
        consulta_async = AsyncResult(task_id,app=app)
        resposta = {
            "resposta" : task_id,
            "estado" : consulta_async.state
        }
        if consulta_async.ready():
            if consulta_async.successful():
                resposta["consulta_async"] = consulta_async.result
            else:
                resposta["erro"] = str(consulta_async.info)
        return resposta
    except Exception as g:
        raise HTTPException(status_code=500,detail=str(g))
