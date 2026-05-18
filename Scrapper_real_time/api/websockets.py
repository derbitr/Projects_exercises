from fastapi import WebSocket,APIRouter,WebSocketDisconnect
from core.logs import registro
import asyncio
from worker.tasks import pegar_dados

logger = registro("WEBSOCKET")
roteador = APIRouter(prefix="/Websocket")

class GerenteConexão:
    def __init__(self):
        self.conexoes_ativas : list[WebSocket] = []
    async def connect(self,websocket : WebSocket):
        await websocket.accept()
        self.conexoes_ativas.append(websocket)
    def disconnect(self,websocket : WebSocket):
        self.conexoes_ativas.remove(websocket)
    async def mensagem_pessoal(self,mensagem : str, websocket : WebSocket):
        await websocket.send_text(mensagem)
    async def broadcast(self,mensagem : str):
        for conexao in self.conexoes_ativas:
            await conexao.send_text(mensagem)
gerente = GerenteConexão()

@roteador.websocket("/ws/")
async def enviar(websocket: WebSocket):
    await gerente.connect(websocket)
    logger.info("Cliente conectado!")
    try:
        while True:
            dados = await websocket.receive_text()
            logger.info(f"Dados recebidos: {dados}")
            tarefa = pegar_dados.delay(dados)
            await gerente.mensagem_pessoal(F"Aguarde..",websocket)
            while not tarefa.ready():
                await asyncio.sleep(1)
            resultado = tarefa.result
            await gerente.mensagem_pessoal(f"Resultado {resultado}",websocket)
    except WebSocketDisconnect as e:
        logger.error(f"Erro: {e}")
        gerente.disconnect(websocket)
        logger.warning("Cliente desconectado")
        await gerente.broadcast(f"Cliente saiu.")

