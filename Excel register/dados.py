import logging

def obter_dados() -> list:
    lista = [
        ["Teclado", 20, 80, 15],
        ["Mouse", 10, 25, 40],
        ["Fone", 15, 20, 30],
        ["Cabo-USB", 30, 40, 80]
    ]
    logging.info("Processando colunas")
    return lista
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    resultado  = obter_dados()
    logging.info("Imprimindo dados")
    print(resultado)

