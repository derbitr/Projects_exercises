from fastapi import APIRouter,FastAPI,HTTPException,Depends
import b1database,b2modelos,b3listasegura,b4jwt,b5auth
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
roteador = APIRouter()
def banco_local():
    banco = b1database.Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
async def verificaçao(token : str = Depends(oauth2_scheme), db: Session = Depends(banco_local)):
    try:
        chaves = b4jwt.jwt.decode(token,b4jwt.CHAVE_SECRETA,algorithms= [b4jwt.ALGORITMO])
        email = chaves.get("sub")
        if email is None:
            raise HTTPException(status_code=401,detail="Inválido")
    except b4jwt.JWTError:
        raise HTTPException(status_code=401,detail="Inválido")
    usuario_db = db.query(b2modelos.Usuario).filter(b2modelos.Usuario.email == email).first()
    if usuario_db is None:
        raise HTTPException(status_code=401,detail="Inválido")
    return usuario_db
@roteador.get("/posts/",response_model=List[b3listasegura.PostResposta])
async def verificar_posts(db: Session = Depends(banco_local)):
    posts = db.query(b2modelos.Post).all()
    return posts
@roteador.post("/posts/",response_model=b3listasegura.PostResposta)
async def criar_post(
    post_in : b3listasegura.PostCriar,
    db : Session = Depends(banco_local),
    usuario_atual : b2modelos.Usuario = Depends(verificaçao)
):
    novo_post = b2modelos.Post(
        titulo = post_in.titulo,
        conteudo = post_in.conteudo,
        autor_id = usuario_atual.id)    
    db.add(novo_post)
    db.commit()
    db.refresh(novo_post)
    return novo_post
