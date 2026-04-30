from fastapi import FastAPI
import uvicorn
from b1redis import broadcast
from b4rotas import app as roteador


app = FastAPI(
    title="Websocket com redis",
    description="Filas assíncronas",
    version=0.6
)

@app.on_event("startup")
async def startup():
    await broadcast.connect()
    return {"Sistema online"}
@app.on_event("shutdown")
async def shutdown():
    await broadcast.disconnect()
    return {"Sistema desligado"}
app.include_router(roteador)

@app.get("/")
async def roteador():
    return {"status":"Online","protocol":"websockets"}
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=6500,reload=True)