import asyncio
import aiohttp
from bs4 import BeautifulSoup
import logging

CABECALHOS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
async def extrair(sessao: aiohttp.ClientSession, url:str) ->dict:
    try:
        async with sessao.get(url , headers=CABECALHOS, timeout=10) as rt:
            if rt.status != 200:
                logging.warning(f"Acesso negado : {rt}")
                return None
            texto_sopa = await rt.text()
            sopa = BeautifulSoup(texto_sopa, "html.parser")
            sopatitulo = sopa.find("h1")
            if not sopatitulo:
                return None
            titulotexto = sopatitulo.text
            precotag = sopa.find("p",class_ = "price_color")
            if not precotag:
                return None 
            preco_limpo = precotag.text.replace("£","").strip()
            preco = float(preco_limpo)
            return {"titulo": titulotexto, "preco" : preco, "link": url }
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")
        return None
async def main():
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    logging.info("Iniciando varredura..")
    async with aiohttp.ClientSession() as sessao:
        resultado = await extrair(sessao, url)
        if resultado:
            logging.info(f"Varredura completa: {resultado}")
        else:
            logging.error("Falha na varredura")
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= '%(levelname)s: %(message)s')
    asyncio.run(main())

        
