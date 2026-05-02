import logging,v4watchdog,v1banco

def iniciar():
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")
    logging.info("Sistema iniciado")
    v1banco.criar_tabela()
if __name__ == "__main__":
    iniciar()
    v4watchdog.sentinela()