import logging
import pandas as pd

def processar(caminho_csv : str) -> pd.DataFrame:
    try:
        df = pd.read_csv(caminho_csv)
        if df.empty:
            logging.warning("Arquivo vazio")
            return None
        df['Faturamento_total'] = df['Units_sold'] * df['Avg_Price_EUR']
        return df
    except FileNotFoundError as e:
        logging.error(f"Ficheiro não encontrado: {e}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    resultado = processar("dados_brutos.csv")
    if resultado is not None:
        print(resultado.head())