from fastapi.responses import StreamingResponse
import a1motor, os, requests
import fastapi
from fastapi import APIRouter,FastAPI,HTTPException,Depends, Header

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_VIDEO_ATUAL = os.path.join(DIRETORIO_ATUAL,"video.mp4")

roteador = APIRouter(prefix="/auth",tags=["Autenticação"])

@roteador.get("/video")
async def video(range : str = Header("bytes=0")):
    try:
        tamanho_real = os.path.getsize(PASTA_VIDEO_ATUAL)
        byte = range.replace("bytes=","")
        inicio, fim = byte.split("-")
        start = int(inicio)
        end = int(fim) if fim else tamanho_real - 1
        try:
            gerador = a1motor.gerador_video(PASTA_VIDEO_ATUAL,start,end)
            return StreamingResponse(gerador,
                    status_code=206,
                    media_type="video/mp4",
                    headers= {"Accept-Ranges": "bytes",
                              "Content-Range": f"bytes {start}-{end}/{tamanho_real}",
                              "Content-Length": str((end - start) + 1)}
                )
        except Exception as f:
            raise HTTPException(status_code=500,detail=str(f))
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))