import pandas as pd
import logging

def limpar(dados : list) -> pd.DataFrame:
    try:
        if not dados:
            logging.warning("Lista de dados vazia ou não existe")
            return
        cabecalho = dados[0]
        linhas = dados[1:]
        df = pd.DataFrame(linhas, columns= cabecalho)
        df = df.dropna(how='all')
        return df
    except Exception as g:
        logging.error(f"Falha ao processar linha de comando : {g}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format='%(levelname)s : %(message)s')
    lista_falsa_do_pdf = [
        ["Produto", "Quantidade", "Preco"],
        ["Teclado", "10", "150.00"],
        [None, None, None],
        ["Rato", "5", "75.50"]
    ]
    resultado = limpar(lista_falsa_do_pdf)
    if resultado is None:
        logging.warning("Tabela vazia")
    else:
        print(resultado)