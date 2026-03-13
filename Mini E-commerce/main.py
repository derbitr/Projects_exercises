import motor_scrapper, Api, scrapper,logging

def config():
    logging.basicConfig(level=logging.INFO, format= '%(levelname)s : %(message)s')
def start():
    dolar = Api.obter_valor()
    if dolar == 0.0:
        logging.error("Erro ao obter o valor")
        return
    links = [
        "https://www.amazon.com/dp/B0741X82H1/",
        "https://www.amazon.com/dp/B08F7PTF53/"
    ]
    links_finais = []
    for link in links:
        precoUSD =  scrapper.busca(link)
        if precoUSD > 0:
            precoBRL = precoUSD * dolar
            precoBRL = round(precoBRL,2)
            links_finais.append([link,precoUSD,precoBRL,dolar])
    if links_finais:
        motor_scrapper.teste(links_finais)
if __name__ == "__main__":
    config()
    logging.info("Iniciando...")
    start()
