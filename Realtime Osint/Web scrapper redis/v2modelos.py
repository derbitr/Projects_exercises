from pydantic import BaseModel, HttpUrl, ValidationError
from typing import Optional, Dict


class ScrapperAlvo(BaseModel):
    url : HttpUrl
    varredura_profunda : bool = False
    prioridade : Optional[bool] = False
    tags : Optional[Dict] = None
class Scrapperresultado(BaseModel):
    url : HttpUrl 
    status_codigo : int
    data : Dict
    error : Optional[str] = None
    sucesso : bool = False
    task_id : str