from pydantic import BaseModel, HttpUrl, ValidationError,Field
from typing import Optional, Dict
from enum import Enum
from datetime import datetime
from uuid import uuid4, UUID
import json


class ModeloTipo(BaseModel):
    Year : int
    Region : str
    Model : str
    Units_Sold : int
    

    def to_json(self) -> str:
        return self.model_dump_json()
    @classmethod
    def from_json(cls,data:str):
        return cls(**json.loads(data))