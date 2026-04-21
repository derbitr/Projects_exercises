import x2modelos,logging
from fastapi.responses import StreamingResponse
import os,requests,x1banco,x2modelos
from fastapi import APIRouter,FastAPI,HTTPException,Depends, Header,Request
from x1banco import url, DIRETORIO_ATUAL, URL_BANCO, PASTA_ATUAL
from sqlalchemy.orm import Session
from x3motor import gerador_video


roteador = APIRouter(prefix="/auth",tags=["Autenticação"])

@roteador.get("/video")
async def video(curso_id : int, request : Request, db : Session = Depends(x1banco.get_db),range_header : str = Header("bytes = 0-1024")):
    try:
        curso = db.query(x2modelos.Curso).filter(x2modelos.Curso.id == curso_id).first()
        if not curso:
            raise HTTPException(status_code=404,detail="Curso não encontrado")
        caminho = curso.caminho_video
        if os.path.getsize(caminho):
            byte = range_header.replace("bytes=","")
            inicio, fim = byte.split("-")
            comecar_video = int(inicio)
            tamanho_total = os.path.getsize(caminho)
            terminar_video = int(fim) if fim else tamanho_total - 1
            try:
                gerador = gerador_video(caminho,comecar_video,terminar_video)
                return StreamingResponse(gerador,
                                status_code=206,
                                media_type="video/mp4",
                                headers={"Accept-Ranges": "bytes",
                                         "Content-Range": f"bytes {comecar_video}-{terminar_video}/{tamanho_total}",
                                         "Content-Length": str((terminar_video - comecar_video) + 1)}
                                         )
            except Exception as f:
                raise HTTPException(status_code=500,detail=str(f))
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))