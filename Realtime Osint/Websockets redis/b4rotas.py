
import asyncio
import b1redis,b2modelos,b3gerente,os,requests,logging
from fastapi import FastAPI, Request, HTTPException, APIRouter,Depends, WebSocket,WebSocketDisconnect
from celery.result import AsyncResult
from uuid import uuid4, UUID
from b1redis import broadcast

manager = b3gerente.Detentor()

app = APIRouter(prefix="/redis",tags=["Tarefas"])

@app.websocket("/ws/{user_id}")
async def enviar (objeto : WebSocket,user_id : UUID ):
    await manager.conectar(objeto , user_id )
    async def motor_enviar():
        try:
            while True:
                dados = await objeto.receive_text()
                if dados:
                    mensagem = b2modelos.EventosRequest.from_json(dados)
                    await broadcast.publish(channel="global",message=mensagem.to_json())
        except WebSocketDisconnect as f:
            pass
    async def motor_receber():
        try:
            async with broadcast.subscribe(channel="global") as subscriber:
                async for evento in subscriber:
                    await manager.mensagens(evento.message, user_id)
        except Exception as h:
            print(f"Ocorreu um erro:{h}")
    try:
        await asyncio.gather(motor_enviar(),motor_receber())
    except Exception as j:
        print(f"Desconectado: {j}")
    finally:
        await manager.desconectar(user_id)
