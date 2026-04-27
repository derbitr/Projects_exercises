import httpx,v1redis,v2modelos,logging,random
from bs4 import BeautifulSoup


def config():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s: %(message)s")


def ClientesWeb(modelo: v2modelos.ScrapperAlvo, resultado : v2modelos.Scrapperresultado):
    lista_navegadores = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.10 Safari/605.1.1",
                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.3",
                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.",
                         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3"]
    lista_navegadores_random = random.choice(lista_navegadores)
    limite_tempo = httpx.Timeout(10.0, connect = 5.0)
    try:
        logging.info("Acessando banco")
        meu_header =    {"User-Agent": lista_navegadores_random}
        with httpx.Client( headers= meu_header,
            timeout=limite_tempo) as cliente:
            resposta = cliente.get(str(modelo.url))
            if resposta.status_code == 200:
                soup = BeautifulSoup(resposta.text, "html.parser")
                soup.get_text(strip=True)
                resultado.data = {"título": soup.title.string, "h1" : soup.find("h1").text }
                resultado.sucesso = True
                resposta.text
            elif resposta.status_code in [429,503]:
                resultado.sucesso = False
                raise Exception("Retry")
            elif resposta.status_code == 404:
                resultado.sucesso = False
                resultado.error = ("Inexistente")
        return resultado
    except Exception as e:
        if str(e) == "Retry":
            raise e
        logging.error(f"Ocorreu um erro: {e}")