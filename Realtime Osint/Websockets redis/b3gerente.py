import socket
from pydantic import BaseModel, HttpUrl, ValidationError,Field
from typing import Optional, Dict
from enum import Enum
from datetime import datetime
from uuid import uuid4, UUID
import json,b2modelos
from fastapi import WebSocket

class Detentor():
    def __init__(self):
        self.conexoes_ativas : Dict = {}
    async def conectar(self, websocket : WebSocket, user_id):
        await websocket.accept()
        self.conexoes_ativas[user_id] = websocket
    async def desconectar(self,user_id):
        try:
            self.conexoes_ativas.pop(user_id)
        except KeyError as e:
            return f"Ocorreu um erro: {e}"
    async def mensagens(self,mensagem,user_id):
        conexao = self.conexoes_ativas.get(user_id)
        if not conexao:
            await self.desconectar(user_id)
        else:
            await conexao.send_json(mensagem)
