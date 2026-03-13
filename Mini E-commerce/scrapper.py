from bs4 import BeautifulSoup
import requests, logging


cabeçalhos= {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 ',
    'Accept-Language': 'en-US ,en;q=0.5'
}
def extraçao(url: str) -> float:
    try:
        pedido = requests.get(url,headers=cabeçalhos,timeout=50)
        if not pedido:
            logging.error("Pedido falhou")
            return 0.0
        if pedido.status_code != 200:
            logging.warning(f"Acesso negado: {pedido.status_code}")
            return 0.0
        try:
            sopa = BeautifulSoup(pedido.content,"html.parser")
            sopa_elemento = sopa.find("span",class_ = "a-offscreen")
            if not sopa_elemento:
                logging.error("Produto não encontrado")
                return 0.0
            preco_texto = sopa_elemento.text
            preco_limpo = preco_texto.replace("$","").replace(",","").strip()
            return  float(preco_limpo)
        except Exception as e:
            logging.error(f"Erro ao converter os preços: {e}")
            return 0.0
    except requests.exceptions.RequestException  as f:
        logging.error(f"Erro de busca encontrado: {f}")
        return 0.0
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    url = "https://www.amazon.com/dp/B0741X82H1/"
    logging.info("Realizando varredura")
    busca =extraçao(url)
    if busca > 0:
        logging.info("Busca realizada")
    print(busca)
