from pydantic import BaseModel, HttpUrl, ValidationError,Field
from typing import Optional, Dict
from enum import Enum
from datetime import datetime
from uuid import uuid4, UUID
import json

class Eventostatus(str,Enum):
    MENSAGEM = "Chat"
    ALERTA = "Alerta de sistema"
    Ping = "Ping"
class EventosRequest(BaseModel):
    remetente_id : UUID = Field(default_factory=uuid4)
    event_type : Eventostatus
    conteudo : any
    timestamp : datetime = Field(default_factory=datetime.now)

    def to_json(self) -> str:
        return self.model_dump_json()
    @classmethod
    def from_json(cls,data : str):
        return cls(**json.loads(data))
