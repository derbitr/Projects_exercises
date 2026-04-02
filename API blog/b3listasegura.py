from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import pydantic

class UsuarioBase(BaseModel):
    username : str = Field(min_length=4)
    email : EmailStr
class UsuarioCriar(UsuarioBase):
    senha : str = Field(min_length=3)
class UsuarioLogin(BaseModel):
    email : EmailStr
    senha : str = Field(min_length=3)
class UsuarioResposta(UsuarioBase):
    id : int
    model_config = {'from_attributes' : True}
class PostBase(BaseModel):
    titulo : str
    conteudo : str
class PostCriar(PostBase):
    pass
class PostResposta(PostBase):
    id : int
    publicado : bool
    autor_id : int
    model_config = {'from_attributes':True}


