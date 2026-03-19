import logging, os
import pdfplumber, p1cleaner,p2extractor,p3generator

def config():
    logging.basicConfig(level=logging.INFO,format= '%(levelname)s: %(message)s')
def start(target : str):
    lista = []
    try:
        for nome_arquivo in os.listdir(target):
            if nome_arquivo.endswith(".pdf"):
                logging.info("Processando arquivo pdf")
                caminho = os.path.join(target,nome_arquivo)
                if caminho is None:
                    logging.warning("Caminho não encontrado")
                tabela_extrair = p2extractor.extrair_tabela(caminho)
                if tabela_extrair:
                    lista.append(tabela_extrair)
        if lista:
            logging.info("Extraindo tabela")
            tabela_limpa = p1cleaner.processar(lista)
            logging.info("Tabela limpa")
            if tabela_limpa is not None:
                logging.info("Dados salvos")
                print(tabela_limpa)
                site = p3generator.construcao(tabela_limpa)
            else:
                logging.warning("Falha na limpeza")
        else:
            logging.warning("Falha ao procurar tabela")
    except Exception as h:
        logging.error(f"Ocorreu um erro: {h}")
if __name__ == "__main__":
    config()
    logging.info("Iniciando...")
    caminho_pasta = r"e:\Downloads opera"
    if os.path.exists(caminho_pasta) and os.path.isdir(caminho_pasta):
        logging.info("Pasta encontrada, iniciando procedimento")
        start(caminho_pasta)
    else:
        logging.warning("Erro ao encontrar página")