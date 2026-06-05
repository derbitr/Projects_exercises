from fastapi import APIRouter,FastAPI,HTTPException,Depends
from core.logs import iniciar_log
from models.false_bank import buscar_email,receber_usuario
from core.security import gerar_senha,verificar_hash,criar_token
from models.schemas import UsuarioCriar
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



roteador = APIRouter()
logger = iniciar_log("Auth")

@roteador.post("/cadastro")
async def verificar_dados(dados:UsuarioCriar):
    try:
        logger.info("Iniciando verificação de dados")
        cadastro_email = buscar_email(dados.email)
        if cadastro_email:
            raise HTTPException(status_code=400,detail="Email já cadastrado")
        else:
            senha_criptografada = gerar_senha(dados.senha)
            dados.senha = senha_criptografada
            dados_dicionario = dados.model_dump()
        receber_usuario(dados_usuario=dados_dicionario)
        return {"mensagem": "Usuário criado com sucesso"}
    except HTTPException as e:
        logger.error(F"Erro encontrado: {e}")
        return
@roteador.post("/login")
async def verificar_login(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.info("Verificando login")
    buscar_usuario = buscar_email(form_data.username)
    if not buscar_usuario:
        raise HTTPException(status_code=401,detail="Credencial inválida")
    senha = verificar_hash(senha_pura=form_data.password,senha_hash=buscar_usuario["senha"])
    if not senha:
        raise HTTPException(status_code=401,detail="Credencial inválida")
    else:
        sub = criar_token({"sub": form_data.username})
        return {"access_token" : sub, "token_type":"bearer"}