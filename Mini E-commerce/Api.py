import requests,logging

def obter_valor()-> float:
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        pedido_url = requests.get(url, timeout=10)
        if pedido_url:
            logging.info("Extraindo dados")
        url_json = pedido_url.json()
        if url_json:
            cotacao = url_json["USDBRL"]["bid"]
            logging.info("Dados selecionados")
            return float(cotacao)
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao buscar os dados: {e}")
        return 0.0
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    resultado = obter_valor()
    if resultado > 0:
        print(resultado)