
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

chave_secreta = os.getenv("CHAVE_SECRETA")
algoritmo = os.getenv("ALGORITMO")
acesso_token_expiracao = int(os.getenv("ACESSO_TOKEN_EXPIRACAO",60))
criptografia = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def gerar_hash(senha:str):
    return criptografia.hash(senha)
def verificar_hash(senha_pura: str, senha_hash : str):
    return criptografia.verify(senha_pura,senha_hash)
def criar_token(dados: dict):
    try:
        dados_copiados = dados.copy()
        if dados_copiados:
            tempo_expiracao = datetime.utcnow() + timedelta(minutes=acesso_token_expiracao)
            dados_copiados.update({"exp": tempo_expiracao})
            token_jwt = jwt.encode(dados_copiados,chave_secreta,algorithm=algoritmo)
            return token_jwt
    except Exception as e:
        print(f"Ocorreu um erro: {e}")