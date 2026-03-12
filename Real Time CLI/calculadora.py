import logging


def calcular(valor_cliente : float, cotacao_cambio : float) -> float:
    if valor_cliente < 0:
        logging.error("Valor não pode ser negativo")
        return 0.0
    if cotacao_cambio <= 0:
        logging.error("Cotação precisa ser maior que zero")
        return 0.0
    resultado_final = round(valor_cliente * cotacao_cambio, 2)
    logging.info("Processando conversão")
    return resultado_final
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    teste = calcular(150.0,5.08)
    if teste > 0:
        logging.info("Teste sucedido")
        print(f"resultado : {teste}")

