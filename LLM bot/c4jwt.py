from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional


CHAVE_SECRETA = "euamomeubot123"
ALGORITMO = "HS256"
ACESSO_TOKEN_EXPIRACAO = 60
criptografia = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def gerar_hash(senha:str):
    return criptografia.hash(senha)
def verificar_hash(senha_pura:str,senha_hash:str):
    return criptografia.verify(senha_pura,senha_hash)
def criar_token(dados:dict):
    try:
        copiar_dados = dados.copy()
        if copiar_dados:
            tempo_expiracao = datetime.utcnow() + timedelta(minutes=ACESSO_TOKEN_EXPIRACAO)
            copiar_dados.update({"exp":tempo_expiracao})
            token_jwt = jwt.encode(copiar_dados,CHAVE_SECRETA,algorithm=ALGORITMO)
            return token_jwt
    except Exception as e:
        return f"Ocorreu um erro: {e}"
