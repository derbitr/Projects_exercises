from fastapi import FastAPI
from api.router import roteador as roteador_http
from api.websockets import roteador as roteador_websocket
import uvicorn

app = FastAPI(
    title="Scrapper_tempo_real",
    description="Leve teste",
    version="1.0"
)
app.include_router(router=roteador_http)
app.include_router(router=roteador_websocket)
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port = 8700, reload= True)


