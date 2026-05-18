import logging,sys

def registro(nome_modulo:str):
    logger =logging.getLogger(nome_modulo)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s :")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
if __name__ == "__main__":
    registro_teste = registro("TESTE")
    registro_teste.info("Sistema funcionando")
