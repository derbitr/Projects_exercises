import logging
import pandas as pd
import dados_sql, analisador

def config():
    logging.basicConfig(level=logging.INFO,format = '%(levelname)s : %(message)s')
def iniciar():
    df_processado = analisador.processar("dados_brutos.csv")
    try:
        if df_processado is None:
            logging.error("Falha ao carregar o dataframe")
            return
        dados_sql.dados(df_processado)
        logging.info("Processo atualizado com sucesso")
    except Exception as e:
        logging.error(f"Falha ao carregar dados : {e}")
        return
if __name__ == "__main__":
    config()
    logging.info("Iniciando sistema...")
    iniciar()
    logging.info("Dados atualizados")
    