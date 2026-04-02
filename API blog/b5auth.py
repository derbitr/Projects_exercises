from fastapi import APIRouter,FastAPI,HTTPException,Depends
import b1database,b2modelos,b3listasegura,b4jwt
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# dados_autenticados : OAuth2PasswordRequestForm = Depends() 
roteador = APIRouter()
def banco_local():
    banco = b1database.Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
@roteador.post("/usuarios/",response_model=b3listasegura.UsuarioResposta)
async def verificar_dados(usuario_interno: b3listasegura.UsuarioCriar,db :Session = Depends(banco_local)):
    senha_protegida = b4jwt.gerar_hash(usuario_interno.senha)
    modelo_banco = b2modelos.Usuario(
        username = usuario_interno.username,
        email = usuario_interno.email,
        senha_hash = senha_protegida
    )
    db.add(modelo_banco)
    db.commit()
    db.refresh(modelo_banco)
    return modelo_banco
@roteador.post("/login/")
async def verificar_login(dados_autenticados: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(banco_local)):
    usuario= db.query(b2modelos.Usuario).filter(b2modelos.Usuario.email== dados_autenticados.username).first()
    if not usuario:
        raise HTTPException(status_code=401,detail="Credenciais inválidas")
    else:
        senha = b4jwt.verificar_hash(dados_autenticados.password,usuario.senha_hash)
    if senha == False:
        raise HTTPException(status_code=401,detail="Credenciais invalidas")
    sub = b4jwt.criar_token_senha({"sub" : usuario.email})
    return {"access_token" : sub, "token_type" : "bearer"}