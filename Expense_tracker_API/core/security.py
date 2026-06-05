from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
import time
from core.config import chave_secreta,algoritmo,acessso_token
from core.logs import iniciar_log
from fastapi import HTTPException

logger = iniciar_log("Segurança")

contexto_bcrypt = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def gerar_senha(senha:str):
    return contexto_bcrypt.hash(senha)
def verificar_hash(senha_pura,senha_hash) -> bool:
    return contexto_bcrypt.verify(senha_pura, senha_hash)
def criar_token(dados:dict):
    try:
        copia_dados = dados.copy()
        if copia_dados:
            tempo_atual = time.time()
            tempo_expirado = datetime.utcnow() + timedelta(minutes=int(acessso_token))
            copia_dados.update({"exp": tempo_expirado})
            token_jwt = jwt.encode(copia_dados,chave_secreta,algorithm=algoritmo)
            return token_jwt
    except Exception as e:
        logger.error(e)
        raise e
def decodificar_token(token:str):
    try:
        validacao_token = jwt.decode(token,chave_secreta,algorithms=[algoritmo])
        if validacao_token:
            return validacao_token["sub"]
        else:
            raise JWTError
    except JWTError as e:
        logger.error(f"Ocorreu um erro: {e}")
        raise HTTPException(status_code=401,detail="token inválido")