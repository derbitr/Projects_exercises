import requests, logging



def cotacao(moeda_origem : str, moeda_destino: str) -> float:
    if not moeda_origem or not moeda_destino:
        logging.warning("Moedas não podem estar vazias")
        return 0.0
    logging.info("Processando pedido...")
    urls = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}".upper().strip()
    try:
        resposta = requests.get(urls, timeout=5)
        resposta.raise_for_status()
        if resposta:
            dados = resposta.json()
            chave = f"{moeda_origem}{moeda_destino}".upper().strip()
            cotas = float(dados[chave]['bid'])
            return cotas
    except requests.exceptions.RequestException as e:
        logging.error(f"Falha ao acessar a rede: {e}")
        return 0.0
    except KeyError as f:
        logging.error(f"Erro de digitação, tente novamente: {f}")
        return 0.0
if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    script = cotacao("USD","BRL")
    if script:
        print(f"Valores convertidos: {script}")
