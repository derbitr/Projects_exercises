import requests; import os; import dotenv; from dotenv import load_dotenv;import logging; 

dotenv.load_dotenv()
def obter_dados(cidade : str) ->tuple:
    if not cidade or not cidade.strip():
        logging.error("Nome de cidade invalido")
        return None,None
    api = os.getenv("MINHA_APYKEY")
    if not api:
        logging.error(f"Chave de api não encontrada")
        return None, None
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&APPID={api}&units=metric"
    try:
        pedido = requests.get(url,timeout=10)
        pedido.raise_for_status()
        dados =pedido.json()
        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        logging.info(f"Clima de {cidade} extraido com sucesso!")
        return temp, descricao
    except requests.exceptions.RequestException as internet_erro:
        logging.error(f"Falha na busca : {internet_erro}")
        return None,None
    except (KeyError,IndexError,TypeError) as erro_dados:
        logging.error(f"Falha na busca da cidade : {erro_dados}")
        return None, None

