import logging, os
import pdfplumber
import extractor,cleaner
def config():
    logging.basicConfig(level=logging.INFO,format= '%(levelname)s : %(message)s')
def start(alvo: str):
    try:
        for nome_arquivo in os.listdir(alvo):
            if nome_arquivo.endswith(".pdf"):
                logging.info("Processando arquivo pdf")
                caminho = os.path.join(alvo,nome_arquivo)
                if caminho is None:
                    logging.warning("Dados nao encontrados")
                tabela = extractor.processador(caminho)
                if tabela:
                    logging.info(f"Sucesso, tabela encontrada e processada vinda de {caminho}")
                    tabela_limpa = cleaner.limpar(tabela)
                    if tabela_limpa is not None and not tabela_limpa.empty:
                        logging.info("Dados limpos")
                        print(tabela_limpa)
                    else:
                        logging.warning("Tabela ficou vazia após a limpeza")
                else:
                    logging.warning("Nenhuma tabela encontrada")
    except Exception as f:
        logging.error(f"Falha ao processar comando : {f}")
        return None
if __name__ == "__main__":
    config()
    logging.info("Iniciando...")
    caminho_pasta = "pdfteste"
    if os.path.exists(caminho_pasta):
        logging.info("Pasta encontrada, iniciando processamento...")
        start(caminho_pasta)
    else:
        logging.warning("Pasta não existe")
