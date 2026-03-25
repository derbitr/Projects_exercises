import pandas, requests,openpyxl, os,logging,time
from datetime import datetime,timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import c2banco

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_VIGIA = os.path.join(DIRETORIO_ATUAL, "Pendências")
if not os.path.exists(PASTA_VIGIA):
    os.makedirs(PASTA_VIGIA)
    logging.info("Pasta vigia criada")
class ManipuladorDespesas(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        caminho_ficheiro = event.src_path
        try:
            nome_ficheiro = os.path.basename(caminho_ficheiro)
            if nome_ficheiro.endswith(".txt"):
                partes = nome_ficheiro.replace(".txt","").split("_")
                valor = float(partes[0])
                categoria = partes[1]
                data_hoje = datetime.now().strftime("%Y-%m-%d")
                c2banco.inserir_dados(valor,categoria,data_hoje)
                logging.info("Dados salvos no banco de dados")
                try:
                    dados_api = {
                        "titulo": f"RPA: {nome_ficheiro}",
                        "valor": valor,
                        "categoria": categoria,
                        "data": data_hoje
                    }
                    try:
                        resposta = requests.post("http://127.0.0.1:8001/items/", json = dados_api)
                        if resposta.status_code == 200:
                            logging.info("Salvo na api")
                        else:
                            logging.warning("Erro ao salvar na api")
                    except Exception as fg:
                        logging.error(f"Erro ao buscar a api: {fg}")
                except Exception as j:
                    logging.error(f"Erro ao buscar dados: {j}")
                logging.info(f"Categoria: {categoria}\nR$: {valor}")
        except Exception as g:
            logging.error(f"Ocorreu um erro: {g}")
            return
    def on_modified(self, event):
        if event.is_directory:
            logging.info(f"Arquivo {event.src_path} foi modificado")
            return
    def on_deleted(self, event):
        if not event.is_directory:
            logging.info(f"Arquivo {event.src_path} foi deletado")
            return
    def on_moved(self, event):
        if event.is_directory:
            logging.info(f"Arquivo {event.src_path} foi movido")
def sentinela():
    logging.info("Iniciando observador de arquivos")
    try:
        event_handler=ManipuladorDespesas()
        observer = Observer()
        observer.schedule(event_handler,path=PASTA_VIGIA,recursive=True)
        observer.start()
        logging.info("Iniciando sistema")
        logging.info("Arraste um arquivo. Pressione CTRL + C no terminal para parar")
        try:
            while True:
                time.sleep(1.5)
        except KeyboardInterrupt:
            observer.stop()
            logging.info("Sistema de observação parado")
        observer.join()
    except Exception as e:
        logging.error(f"Erro ao iniciar observador: {e}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format = "%(asctime)s : %(message)s", datefmt= "%H/%M/%S")
    sentinela()