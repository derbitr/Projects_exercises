import precos, motor
import logging, asyncio, aiohttp

def config():
    logging.basicConfig(level=logging.INFO,format='%(levelname)s : %(message)s')
async def iniciar():
    lista_alvo = [
        "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
    "http://books.toscrape.com/catalogue/soumission_998/index.html",
    "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
    ]
    try:
        async with aiohttp.ClientSession() as sessao:
            lista = []
            for link in lista_alvo:
                lista.append(precos.extrair(sessao,link))
            lista_resultado = await asyncio.gather(*lista)
            lista_resultado_filtrados = [ item for item in lista_resultado if item is not None]
            if lista_resultado_filtrados:
                motor.comparar(lista_resultado_filtrados)
            else:
                logging.error("Erro ao comparar dados")
    except Exception as e:
        logging.error(f"Erro na sincronização: {e}")
if __name__ == "__main__":
    config()
    logging.info("Iniciando sistema...")
    asyncio.run(iniciar())
