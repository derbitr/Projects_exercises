import logging
def config():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s : %(message)s")
def gerador_video(caminho_arquivo : str,inicio : int, fim : int, tamanho_arquivo : int =  1024*1024  ):
    try:
        logging.info("Iniciando tentativa de leitura de arquivo")
        with open (caminho_arquivo, "rb") as arquivo:
            cursor = arquivo.seek(inicio)
            while arquivo.tell() <= fim:
                faltam = fim - arquivo.tell() + 1
                tamanho_leitura = min(tamanho_arquivo, faltam)
                leitura = arquivo.read(tamanho_leitura)
                if not leitura:
                    logging.warning("arquivo vazio")
                    break
                yield leitura
    except Exception as e:
        logging.error(f"Erro inesperado : {e}")
if __name__ == "__main__":
    config()
    gerador_video()