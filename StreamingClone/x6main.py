from fastapi import FastAPI
import x1banco,x2modelos,x3motor,x3motorrotas,x5rotafinanceira,x4estoque
import uvicorn,logging


def config():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s : %(message)s")

app = FastAPI(
    title="copia boba da logica por trás de streaming/loja",
    description="falei ali em cima",
    version="1.0"
)
x1banco.Base.metadata.create_all(bind = x1banco.motor)

app.include_router(x3motorrotas.roteador)
app.include_router(x5rotafinanceira.roteador)
@app.on_event("startup")
async def testar_inicio():
    db = x1banco.Sessao_local()
    try:
        if not db.query(x2modelos.Curso).first():
            logging.info("Criando")
            novo_curso = x2modelos.Curso(
                titulo = "Curso de soldagem",
                preco = 99.5,
                vagas_disponiveis = 5,
                caminho_video = "video_teste.mp4"
            )
            db.add(novo_curso)
            db.commit()
    finally:
        db.close()
@app.get("/")
async def iniciar():
    return {"status": "Ta com sinal ( eu acho )"}
if __name__ == "__main__":
    config()
    logging.info("Iniciandos")
    uvicorn.run(app,host="127.0.0.1",port=8008)