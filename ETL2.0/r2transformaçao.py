import pandas as pd
import logging
import r1extraçao

def analisar(caminho_venda : str):
        try:
            logging.info("Iniciando tranformaçao")
            df = pd.read_excel(caminho_venda)
            if not df.empty:
                logging.info("DataFrame criado")
                df['Faturamento'] = df['Quantidade'] * df['Preco_Unitario']
                resumo_vendedores = df.groupby("Vendedor")["Faturamento"].sum()
                return resumo_vendedores,df
            else:
                return None,None
        except Exception as f:
            logging.error(f"Ocorreu um erro: {f}")
            return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= '%(levelname)s : %(message)s')
    excel = analisar("vendas_brutas.xlsx")
    if excel:
        logging.info("Excel transformado")
    else:
        logging.warning("Falha ao transformar excel")

