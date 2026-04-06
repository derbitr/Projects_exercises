import c1banco,c2modelos,c3moldes,c4jwt,c5IA
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter,FastAPI,HTTPException,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

oauth2_chave = OAuth2PasswordBearer(tokenUrl="/auth/login")
roteador = APIRouter(prefix="/auth",tags=["Autenticação"])
def banco_local():
    banco = c1banco.Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
@roteador.post("/registrar",response_model=c3moldes.UsuarioResposta)
async def verificar_dados(novo_usuario : c3moldes.UsuarioCriar,db : Session = Depends(banco_local)):
    try:
        usuario_email = db.query(c2modelos.Usuario).filter(c2modelos.Usuario.email == novo_usuario.email).first()
        if usuario_email:
            raise HTTPException(status_code=400,detail="Usuário já cadastrado")
        senha_segura = c4jwt.gerar_hash(novo_usuario.senha)
        if not senha_segura:
            raise HTTPException(status_code=401,detail="Senha inválida")
        usuario_db = c2modelos.Usuario(
            username = novo_usuario.username,
            email = novo_usuario.email,
            senha_hash = senha_segura
        )
        db.add(usuario_db)
        db.commit()
        db.refresh(usuario_db)
        return usuario_db
    except Exception as j:
        raise HTTPException(status_code=500,detail=str(j))

@roteador.post("/login/")
async def verificar_login(autenticar_login : OAuth2PasswordRequestForm = Depends(),db : Session = Depends(banco_local)):
    try:
        usuario_no_banco = db.query(c2modelos.Usuario).filter(c2modelos.Usuario.email == autenticar_login.username).first()
        if not usuario_no_banco:
            raise HTTPException(status_code=400,detail="Usuário não encontrado")
        comparar_senha = c4jwt.verificar_hash(autenticar_login.password,usuario_no_banco.senha_hash)
        if comparar_senha == False:
            raise HTTPException(status_code=401,detail="Credenciais inválidas")
        sub = c4jwt.criar_token({"sub": usuario_no_banco.email})
        return {"access_token":sub , "token_type": "bearer"}
    except Exception as h:
        raise HTTPException(status_code=500,detail=str(h))
async def verificação_bot(token: str = Depends(oauth2_chave),db : Session = Depends(banco_local)):
    try:
        chave = c4jwt.jwt.decode(token, c4jwt.CHAVE_SECRETA,algorithms=[c4jwt.ALGORITMO])
        usuario = chave.get("sub")
        if usuario is None:
            raise HTTPException(status_code=401,detail="Usuário não encontrado")
        usuario_db = db.query(c2modelos.Usuario).filter(c2modelos.Usuario.email == usuario).first()
        if usuario_db is None:
            raise HTTPException(status_code=401,detail="Inválido")
        return usuario_db
    except c4jwt.JWTError as e:
        raise HTTPException(status_code=401,detail=str(e))
    
@roteador.post("/chat/enviar")
async def verificação(pergunta : c3moldes.ChatEntrada, usuario_atual : c2modelos.Usuario = Depends(verificação_bot),db : Session = Depends(banco_local)):
    try:
        motor = await c5IA.traducao_bot(usuario_interno=usuario_atual,pergunta=pergunta,db = db)
        if not motor:
            raise HTTPException(401,detail="Ocorreu um erro")
        return motor
    except Exception as j:
        raise HTTPException(status_code=500,detail= str(j))