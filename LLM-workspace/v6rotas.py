import v1banco,v2modelos,v3moldes,v4jwt,v5ia
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm,HTTPBearer,HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter,FastAPI,HTTPException,Depends




#Funções da API
oauth_chave = OAuth2PasswordBearer(tokenUrl="/auth/login") #Variável que vai passar a chave hash
roteador = APIRouter(prefix="/auth",tags=["Autenticação"]) #Variável que vai ligar o roteador da APi
def banco_local():
    banco = v1banco.Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
@roteador.post("/registrar",response_model=v3moldes.UsuarioResposta)
async def verificar(novo_usuario:v3moldes.UsuarioCriar,db:Session = Depends(banco_local)):
    try:
        usuario_email = db.query(v2modelos.Usuario).filter(v2modelos.Usuario.email ==novo_usuario.email).first()
        if usuario_email:
            raise HTTPException(status_code=400, detail = "Usuário já cadastrado")
        senha_protegida = v4jwt.gerar_hash(novo_usuario.senha)
        if not senha_protegida:
            raise HTTPException(status_code=401,detail ="Senha inválida")
        usuario_no_db = v2modelos.Usuario(
            username = novo_usuario.username,
            email = novo_usuario.email,
            senha_hash = senha_protegida
        )
        db.add(usuario_no_db)
        db.commit()
        db.refresh(usuario_no_db)
        return usuario_no_db
    except Exception as j:
        raise HTTPException(status_code=500, detail=str(j))

@roteador.post("/login/")
async def verificar_login(autenticar_login: OAuth2PasswordRequestForm = Depends(),db : Session = Depends(banco_local)):
    try:
        usuariodb = db.query(v2modelos.Usuario).filter(v2modelos.Usuario.email == autenticar_login.username).first()
        if not usuariodb:
            raise HTTPException(status_code=400,detail="Usuário nao encontrado")
        comparar_senha = v4jwt.verificar_hash(autenticar_login.password,usuariodb.senha_hash)
        if comparar_senha == False:
            raise HTTPException(status_code=401,detail="Credenciais inválidas")
        sub = v4jwt.criar_token({"sub":usuariodb.email})
        return {"access_token":sub,"token_type":"bearer"}
    except Exception as h:
        raise HTTPException(status_code=500,detail=str(h))
async def verificar_ia(token : str = Depends(oauth_chave),db : Session = Depends(banco_local)):
    try:
        chave = v4jwt.jwt.decode(token,v4jwt.chave_secreta,algorithms=[v4jwt.algoritmo])
        usuario = chave.get("sub")
        if usuario is None:
            raise HTTPException(status_code=401,detail="Usuário não encontrado")
        usuario_db = db.query(v2modelos.Usuario).filter(v2modelos.Usuario.email ==usuario).first()
        if usuario_db is None:
            raise HTTPException(status_code=401,detail="Usuário Inválido")
        return usuario_db
    except Exception as h:
        raise HTTPException(status_code=401,detail=str(h))

@roteador.post("/chat/enviar")
async def verificação(pergunta : v3moldes.ChatEntrada,usuario_atual : v2modelos.Usuario = Depends(verificar_ia), db : Session = Depends(banco_local)):
    try:
        motor = await v5ia.traducao_bot_ia(usuario_interno=usuario_atual,pergunta=pergunta,db=db)
        if not motor:
            raise HTTPException(status_code=401,detail="Ocorreu um erro")
        return motor
    except Exception as k:
        raise HTTPException(status_code=500,detail=str(k))

@roteador.post("/tarefas",response_model=v3moldes.TarefaResposta)
async def criar_tarefa(tarefa : v3moldes.TarefaCriar, usuario : v2modelos.Usuario = Depends(verificar_ia), db: Session = Depends(banco_local) ):
    try:
        nova_tarefa = v2modelos.Tarefa(
            titulo = tarefa.titulo,
            dono_id = usuario.id
        )
        db.add(nova_tarefa)
        db.commit()
        return nova_tarefa
    except Exception as k:
        raise HTTPException(status_code=500,detail=str(k))
@roteador.get("/tarefas",response_model=List[v3moldes.TarefaResposta])
async def receber_tarefa(usuario:v2modelos.Usuario = Depends(verificar_ia),db : Session = Depends(banco_local)):
    try:
        tarefas = db.query(v2modelos.Tarefa).filter(v2modelos.Tarefa.dono_id == usuario.id).all()
        return tarefas
    except Exception as ee:
        raise HTTPException(status_code=500,detail=str(ee))
