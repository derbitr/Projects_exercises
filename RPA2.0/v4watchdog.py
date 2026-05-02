import pandas, requests,openpyxl, os,logging,time
from datetime import datetime,timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import v1banco,v2modelos,v3processadorpandas,v5exportadorexcel

DIRETORIO = v1banco.DIRETORIO_ATUAL
PASTA_VIGIA = os.path.join(DIRETORIO,"Pendências")
if not os.path.exists(PASTA_VIGIA):
    os.makedirs(PASTA_VIGIA)
    logging.info("Pasta criada")
class ManipulaçaoAPI(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if not event.src_path.endswith(".csv"):
            return
        caminho_ficheiro = event.src_path
        nome_ficheiro = os.path.basename(caminho_ficheiro)
        logging.info(f"Processando ficheiro: {nome_ficheiro}")
        try:
            dados = v3processadorpandas.logica(caminho_ficheiro)
            if dados:
                inserir = v1banco.inserir_dados(dados)
                nuvem = v1banco.enviar_nuvem(dados)
                dados_excel = v5exportadorexcel.dados_excel(dados,nome_ficheiro)
        except Exception as j:
            logging.error(F"Erro encontrado: {j}")
            return False
    def on_modified(self, event):
        logging.info(f"Arquivo {event.src_path} foi modificado")
        return
    def on_deleted(self, event):
        logging.info(f"Arquivo {event.src_path} foi deletado")
        return
    def on_moved(self, event):
        logging.info(F"Arquivo {event.src_path} foi movido")
        return
def sentinela():
    logging.info("Iniciando sentinela")
    try:
        event_handler = ManipulaçaoAPI()
        observer= Observer()
        observer.schedule(event_handler,path=PASTA_VIGIA,recursive=True)
        observer.start()
        logging.info("Iniciando")
        logging.info("Arraste um arquivo. Pressione CTRL + C no terminal para parar")
        try:
            while True:
                time.sleep(1.5)
        except KeyboardInterrupt:
            observer.stop()
            logging.info("Sistema parado")
        observer.join()
    except Exception as f:
        logging.error(F"Erro ao iniciar o sentinela: {f}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format = "%(asctime)s : %(message)s" , datefmt="%H/%M/%S")
    sentinela()