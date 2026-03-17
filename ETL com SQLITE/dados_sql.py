import sqlite3
import pandas as pd
import logging


def dados(df: pd.DataFrame,nome_banco:str = "empresa.db"):
    try:
        if df is None or df.empty:
            logging.error("Ficheiro vazio")
            return
        conexao = sqlite3.connect(nome_banco)
        try:
            logging.info("Salvando dados no banco")
            df.to_sql(name="vendas_filtradas", con=conexao, if_exists="replace",index=False)
            conexao.close()
            logging.info("Dados salvos no banco")
        except Exception as f:
            logging.error(f"Erro ao salvar dados: {f}")
            return
    except Exception as g:
        logging.error(f"Falha na tentativa de acessar os dados: {g}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')
    dados_teste = pd.DataFrame({
        "Produto": ["Teclado", "Rato"],
        "Units_sold": [10, 5],
        "Faturamento_total": [150.0, 75.0]
    })
    logging.info("Carregando dados...")
    dados(dados_teste)

