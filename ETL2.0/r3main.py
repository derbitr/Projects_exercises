import pandas as pd
import os,r2transformaçao
import logging

def exportar(caminho_origem:str,caminho_destino:str):
    try:
        logging.info("Iniciando sistema")
        origem,destino  = r2transformaçao.analisar(caminho_origem)
        if origem is not None and destino is not None:
            try:
                with pd.ExcelWriter(caminho_destino,engine='openpyxl') as excel:
                    destino.to_excel(excel,sheet_name="Vendas")
                    origem.to_excel(excel,sheet_name="Resumo Vendedor")
                logging.info("Excel salvo")
                return True
            except Exception as g:
                logging.error(f"Erro ao salvar excel : {g}")
                return False
    except Exception as h:
        logging.error(f"Erro ao iniciar o sistema: {h}")
        return False
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    arquivo_origem = os.path.join(diretorio_atual,"vendas_brutas.xlsx")
    arquivo_destino = os.path.join(diretorio_atual,"relatorio.xlsx")
    resultado = exportar(arquivo_origem,arquivo_destino)
    if resultado:
        logging.info("Sucesso")
    else:
        logging.warning("Erro")
