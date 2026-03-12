import cliente_api, calculadora, logging
def config():
    logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')
def iniciar():
    logging.info("Iniciando sistema de conversão simples")
    moeda_origem = input("Selecione 1 cotação: BRL, USD ou EUR: ")
    moeda_destino = input("Seleciona 1 cotação: BRL, USD ou EUR: ")
    if moeda_destino == moeda_origem:
        logging.error("Insira diferentes cotações")
        return
    try:
        valor = input("Insira o valor para processar: ")
        valor = valor.replace(",",".")
        valor_final = float(valor)
        cotacao_atual = cliente_api.cotacao(moeda_origem,moeda_destino)
        if cotacao_atual == 0.0:
            logging.error("Falha ao obter a cotação. Operaçao cancelada")
            return
    except ValueError:
        logging.error("Insira apenas numeros válidos.")
        return
    cotacao_final = calculadora.calcular(valor_final,cotacao_atual)
    logging.info(f"$ {valor_final} {moeda_origem} equivalem a {cotacao_final} {moeda_destino} (Cotação: {cotacao_atual})")
if __name__ == "__main__":
    config()
    logging.info("Inicializando")
    iniciar()    
