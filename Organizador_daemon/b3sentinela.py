import time, logging; import b1classificador,b2movimentador
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            logging.info(f"Arquivo {event.src_path} foi modificado")
            return
        caminho = event.src_path
        logging.info(f"Arquivo {caminho} foi modificado")
    def on_created(self, event):
        if event.is_directory:
            logging.info(f"Arquivo {event.src_path} foi criado")
            return
        caminho = event.src_path
        logging.info(f"Arquivo {caminho} foi criado")
        time.sleep(1.5)
        try:
            categoria = b1classificador.leitor_arquivos(caminho)
            cofre = "Pasta_organizada"
            sucesso = b2movimentador.organizar_arquivo(caminho,cofre,categoria)
            if sucesso:
                logging.info("Operação concluída")
        except Exception as e:
                logging.error(f"Ocorreu um erro {e}")
    def on_deleted(self, event):
        if event.is_directory:
            logging.info(f"Arquivo {event.src_path} foi deletado")
            return
        caminho = event.src_path
        logging.info(f"Arquivo {caminho} foi deletado")
    def on_moved(self, event):
        if event.is_directory:
            logging.info(f"Arquivo {event.src_path} foi movido")
            return
        caminho = event.src_path
        logging.info(f"Arquivo {caminho} foi movido")
