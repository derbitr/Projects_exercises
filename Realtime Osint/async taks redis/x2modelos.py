from pydantic import BaseModel, Field
from uuid import uuid4, UUID
from datetime import datetime
from enum import Enum
import json

class Taskstatus(str,Enum):
    PENDING = "aguardando"
    PROCESSING = "processando"
    COMPLETED = "completado"
    FAILED = "falha"
class TaskRequest(BaseModel):
    task_type : str
    payload: dict
class Taskmodel(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    task_type : str
    payload : dict
    status : Taskstatus = Taskstatus.PENDING
    created_at : datetime = Field(default_factory=datetime.now)
    
    def to_json(self) -> str:
        return self.model_dump_json()
    @classmethod
    def from_json(cls,data: str):
        return cls(**json.loads(data))

    