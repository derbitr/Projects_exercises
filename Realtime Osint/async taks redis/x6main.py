from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import x1redis,x2modelos,x3motor,x4rotas,x5services


app = FastAPI(
    title="Tarefas assíncronas",
    description="Mini projeto para fixar conteúdo sobre API",
    version="1.0"
)
app.add_middleware(CORSMiddleware,
                   allow_origins = ["*"],
                   allow_credentials= True,
                   allow_methods = ["*"],
                   allow_headers = ["*"],)

app.include_router(x4rotas.roteador)      

@app.on_event("startup")
async def iniciar():
    x1redis.get_redis()
    return "Sistema sendo iniciado"

@app.on_event("shutdown")
async def desligar():
    return "Desligando sistema"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("x6main:app",host="127.0.0.1",port=8009,reload=True)