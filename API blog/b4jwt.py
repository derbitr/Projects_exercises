from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
import time,logging

CHAVE_SECRETA = "eunasciamanha123456789"
ALGORITMO = "HS256"
ACESSO_TOKEN_EXPIRACAO = 30

contexto_bcrypt = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def gerar_hash(senha:str):
    return contexto_bcrypt.hash(senha)
def verificar_hash(senha_pura , senha_hash)-> bool:
    return contexto_bcrypt.verify(senha_pura,senha_hash)
def criar_token_senha(dados:dict):
    try:
        copia_dados = dados.copy()
        if copia_dados:
            tempo_atual = time.time()
            tempo_expiracao = datetime.utcnow() + timedelta(minutes=ACESSO_TOKEN_EXPIRACAO)
            copia_dados.update({"exp": tempo_expiracao}) #I had difficult in this part
            token_jwt = jwt.encode(copia_dados,CHAVE_SECRETA,algorithm=ALGORITMO)
            return token_jwt
    except Exception as e:  
        return f"Ocorreu um erro {e}"
