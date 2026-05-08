from pydantic import BaseModel, HttpUrl, ValidationError,Field, ValidationInfo, field_validator, model_validator
from typing import Optional, Dict
from enum import Enum
from datetime import datetime
from uuid import uuid4, UUID
import json


class ModeloBanco(BaseModel):
    Ano : int
    Ticker : str
    Volume : int
    Date : str
    Open : float
    High : float
    Low : float
    Close : float
    @field_validator('Open', 'High', 'Low', 'Close', 'Volume')
    def verificação(cls,v,info : ValidationInfo):
        if info.field_name == "Volume":
            if v >= 0:
                return v
            else:
                raise ValueError
        if info.field_name in ('Open', 'High','Low', 'Close'):
            if v > 0:
                return v
            else:
                raise ValueError
    @model_validator(mode="after")
    def diferença(self):
        if self.High < self.Low:
            raise ValueError
    def to_json(self) -> str:
        return self.model_dump_json()
    @classmethod
    def from_json(cls,data:str):
        return cls(**json.loads(data))
    def to_tuple(self):
        return (self.Ano, self.Ticker,self.Volume,self.Date,self.Open,self.High,self.Low,self.Close)