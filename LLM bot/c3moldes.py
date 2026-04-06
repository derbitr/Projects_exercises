from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import pydantic

class UsuarioBase(BaseModel):
    username : str = Field(min_length=3)
    email :EmailStr
class UsuarioCriar(UsuarioBase):
    senha : str = Field(min_length=3)
class UsuarioLogin(BaseModel):
    email : EmailStr
    senha : str = Field(min_length=3)
class UsuarioResposta(UsuarioBase):
    id : int
    model_config = {"from_attributes": True}
class TarefaCriar(BaseModel):
    titulo : str = Field(min_length=3)
class TarefaResposta(TarefaCriar):
    model_config = {"from_attributes":True}
class ChatEntrada(BaseModel):
    mensagem : str = Field(min_length=1)
class ChatResposta(BaseModel):
    resposta : str = Field(min_length=1)
class MensagemResposta(BaseModel):
    id : int
    papel : str
    conteudo : str
    model_config = {"from_attributes":True}
    