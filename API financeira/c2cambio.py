import requests, time,logging,json,platform

cache_cambio = {
    "cotacao" : 0.0,
    "ultima_atualizacao": 0.0
}
TEMPO_EXPIRAÇÃO = 600

def obter_cotacao()->float:
    tempo_atual = time.time()
    if tempo_atual - cache_cambio["ultima_atualizacao"] < TEMPO_EXPIRAÇÃO:
        logging.info("Cache usado")
        return cache_cambio["cotacao"]
    else:
        logging.error("Cache vazio, fazendo pedido na URL")
        try:
            pedido = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL",timeout=10)
            pedido.raise_for_status()
            pedido_json = pedido.json()
            dados = pedido_json["USDBRL"]["bid"]
            dados_convertidos = float(dados)
            cache_cambio["cotacao"] = dados_convertidos
            tempo_agora = time.time()
            cache_cambio["ultima_atualizacao"] = tempo_agora
            return dados_convertidos
        except requests.exceptions.RequestException as e:
            logging.error(f"Ocorreu um erro de internet: {e}")
            return 5.00
        except (KeyError,IndexError,TypeError) as erro_dados:
            logging.error(f"Falha na busca de dados: {erro_dados}")
            return 5.00




