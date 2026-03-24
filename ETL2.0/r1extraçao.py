import pandas as pd
import os
import logging
def relatorio():
    try:
        logging.info("Iniciando extração de dados")
        dados = {
            "Data": ["2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02", "2026-03-03"],
        "Vendedor": ["Ana", "Carlos", "Ana", "Ana", "Carlos"],
        "Produto": ["Teclado", "Rato", "Monitor", "Teclado", "Monitor"],
        "Quantidade": [5, 10, 2, 3, 1],
        "Preco_Unitario": [45.0, 25.0, 350.0, 45.0, 350.0]
        }
        if dados:
            df = pd.DataFrame(dados)
            diretorio = os.path.dirname(os.path.abspath(__file__))
            caminho  = os.path.join(diretorio,"vendas_brutas.xlsx")
            if caminho:
                df.to_excel(caminho,index=False)
                logging.info("Extração concluída")
                return caminho
            else:
                logging.warning("Erro ao extrair")
                return None
        else:
            logging.warning("Dados não encontrados para extração")
            return None
    except Exception as e:
        logging.error(f"Erro ao iniciar : {e}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    resultado = relatorio()
    if resultado:
        logging.info("Dados extraídos")