import x2modelos,logging
from fastapi.responses import StreamingResponse
import os,requests,x1banco,x2modelos
from fastapi import APIRouter,FastAPI,HTTPException,Depends, Header
from x1banco import url, DIRETORIO_ATUAL, URL_BANCO, PASTA_ATUAL
from sqlalchemy.orm import Session



def config():
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")

def gerador_video(inicio : int, fim : int,caminho_arquivo : str, tamanho_arquivo : int = 1024*1024):
    try:
        logging.info(f"Iniciando leitura : {caminho_arquivo} | Bytes : {inicio}|{fim}")
        with open (caminho_arquivo, "rb") as arquivo:
            arquivo.seek(inicio)
            while arquivo.tell() <= fim:
                faltam = fim - arquivo.tell() + 1
                tamanho_leitura = min (tamanho_arquivo,faltam)
                leitura = arquivo.read(tamanho_leitura)
                if not leitura:
                    logging.warning("Arquivo vazio")
                    break
                yield leitura
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")