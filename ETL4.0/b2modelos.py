from pydantic import BaseModel, HttpUrl, ValidationError,Field, ValidationInfo, field_validator, model_validator
from typing import Optional, Dict
from enum import Enum
from datetime import datetime
from uuid import uuid4, UUID
import json

class ETLbanco(BaseModel):
    Ano : int
    Data : str
    Nome : str
    Altura : float
    Cargo : str
    @field_validator("Ano","Nome","Altura")
    def verificar_altura(cls,a,info:ValidationInfo):
        if info.field_name == "Ano":
            if a >= 2000 and a <= 2100:
                return a
            else:
                raise ValueError
        if info.field_name == "Nome":
            if a != "" and len(a) > 3:
                return a
            else:
                raise ValueError
        if info.field_name == "Altura":
            if a > 0 and a <=3:
                return a
            else:
                raise ValueError
    def to_json(self) -> str:
        return self.model_dump_json()
    @classmethod
    def from_json(cls,data:str):
        return cls(**json.loads(data))
    def to_tuple(self):
        return (self.Ano,self.Data,self.Nome,self.Altura,self.Cargo)