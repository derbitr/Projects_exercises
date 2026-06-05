from pydantic import BaseModel, HttpUrl, ValidationError,Field, ValidationInfo, field_validator, model_validator,EmailStr
from typing import Optional, Dict
from enum import Enum

class UsuarioCriar(BaseModel):
    email : EmailStr
    senha : str = Field(min_length=6)
class DespesaCriar(BaseModel):
    titulo : str
    valor : float = Field(ge=0.0)
    categoria : str
    @field_validator("titulo","valor")
    def verificar_informacoes(cls,i,info:ValidationInfo):
        if info.field_name == "titulo":
            if len(i) > 0:
                return i
            else:
                raise ValueError
        if info.field_name == "valor":
            if i >= 0:
                return i
            else:
                raise ValueError