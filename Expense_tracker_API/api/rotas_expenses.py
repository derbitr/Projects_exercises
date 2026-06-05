from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter,FastAPI,HTTPException,Depends
from api.rotas_auth import roteador
from core.security import decodificar_token, iniciar_log

logger = iniciar_log("Auth_despesas")
roteador_pendencias = APIRouter(prefix="/despesas",tags=["Despesas"])
esquema_oauth2 = OAuth2PasswordBearer(tokenUrl="login")

def obter_usuario(token : str = Depends(esquema_oauth2)):
    decodificador = decodificar_token(token)
    return decodificador
@roteador_pendencias.post("/")
async def despesas(dados: dict, usuario : str = Depends(obter_usuario)):    
    logger.info(usuario)
    return {"mensagem": "Acesso liberado",
            "usuario": usuario,
            "despesa": dados}
