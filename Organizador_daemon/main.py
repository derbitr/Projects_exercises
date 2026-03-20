import time, logging, os
from watchdog.observers import Observer
from b3sentinela import Myhandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= '%(asctime)s : %(message)s', datefmt= '%H:%M:%S')
    pasta = r"e:\Downloads opera"
    if os.path.exists(pasta):
        logging.info("Selecionando arquivos na pasta")
    else:
        os.makedirs(pasta,exist_ok=True)
        logging.info("Pasta criada")
    event_handler = Myhandler()
    observer = Observer()
    observer.schedule(event_handler, path=pasta, recursive=True)
    observer.start()
    logging.info("Iniciando sistema")
    logging.info("Arraste um arquivo. Pressione CTRL+C no terminal para parar")
    try:
        while True:
            time.sleep(1.5)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("DAEMON PARADO")
    observer.join() 