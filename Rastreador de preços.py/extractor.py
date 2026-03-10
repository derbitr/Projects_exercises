
import requests, logging
from bs4 import BeautifulSoup

def extrair_datas(url : str) ->tuple:
    if not url or not url.strip():
        return None,None
    cabecalho = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64 ; x64)AppleWebKit/537.36(KHTML, like gecko) Chrome/120.0.0.0 Safari/537.36 "}
    try:
        pedido = requests.get(url, headers=cabecalho, timeout= 10)
        pedido.raise_for_status() 
        soup = BeautifulSoup(pedido.text, 'html.parser')
        preco = soup.find('p',class_= 'price_color')
        preco = preco.text.strip() if preco else "sem valor"
        titulo = soup.title.text.strip()
        return titulo, preco
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro de rede: {e}")
        return None,None
    except AttributeError as f:
        logging.error(f"Erro de busca de dados: {f}")
        return None,None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    t,p = extrair_datas("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    print(f"Produto: {t}")
    print(f"Preço : {p}")
    
