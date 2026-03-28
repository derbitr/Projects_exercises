from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random,uvicorn,fastapi,c2cambio
import string
import logging


banco_urls = {}
def log():
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")
api = FastAPI(title="API financeira",version="1.0")

def gerar_codigo(tamanho: int = 6):
    caracteres = string.ascii_letters + string.digits
    return "".join(random.choices(caracteres,k=tamanho))
@api.get("/")
def home():
    return {"Mensagem": "Bem-vindo a API fincanceira"}
@api.post("/encurtar")
def encurtar_url(url_original:str):
    codigo = gerar_codigo()
    banco_urls[codigo] = url_original
    logging.info(f"Url encurtada: {codigo} = {url_original}")
    url_curta =f"http://127.0.0.1:8003/{codigo}"
    return {
        "url_original": url_original,
        "url_curta": url_curta,
        "codigo": codigo
    }
@api.get("/{codigo}")
def redirecionar(codigo:str):
    if codigo in banco_urls:
        url_destino = banco_urls[codigo]
        logging.info(f"Usuario redirecionado: {url_destino}")
        return RedirectResponse(url=url_destino)
    else:
        raise HTTPException(status_code=404,detail="Url não encontrada")
@api.get("/premio/{pontos:int}")
def calcular_premio(pontos:int):
    cotacao_atual = c2cambio.obter_cotacao()
    try:
        premio_dolar = float(pontos)
        logging.info("Premio dolar convertido")
        premio_real = premio_dolar * cotacao_atual
        logging.info("Premio em real convertido")
        url_premio = f"https://financeiro.com/trofeu?pontos={pontos}&brl={premio_real:.2f}"
        codigo_curto = gerar_codigo()
        banco_urls[codigo_curto] = url_premio
        url_premio_curta = f"http://127.0.0.1:8003/{codigo_curto}"
        return {
            "Pontos" : pontos,
            "Prêmio em dólar" : premio_dolar,
            "Cotação usada" : cotacao_atual,
            "Prêmio em real" : premio_real,
            "Link para compartilhar" : url_premio_curta
            }
    except Exception as f:
        logging.error(f"Ocorreu um erro: {f}")
        return
if __name__ == "__main__":
    log()
    logging.info("Iniciando api")
    uvicorn.run(api,host="127.0.0.1",port=8003)