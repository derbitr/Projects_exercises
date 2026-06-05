import logging,sys

def iniciar_log(arquivo : str):
    logger = logging.getLogger(arquivo)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s : ")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
if __name__ == '__main__':
    teste = iniciar_log("TESTE")
    teste.info("sistema iniciado")
    