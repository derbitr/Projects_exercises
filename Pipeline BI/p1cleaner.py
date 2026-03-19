import pandas as pd
import logging

def processar (lista_tabelas: list) -> dict:
    try:
        if not lista_tabelas:
            logging.warning("Lista vazia")
            return None
        try:
            tabela = lista_tabelas[0]
            cabecalho = tabela[0]
            linhas = tabela[1:]
            df = pd.DataFrame(linhas,columns=cabecalho)
            df = df.dropna(how='all')
            df['Quantidade'] = pd.to_numeric(df['Quantidade'],errors='coerce').fillna(0)
            df['Preco'] = pd.to_numeric(df['Preco'].astype(str).str.replace(',','.').str.strip(),errors ='coerce').fillna(0)
            df['Receita'] = df['Quantidade'] * df['Preco']
            faturamento = df['Receita'].sum()
            df_grouby = df.groupby('Produto',as_index=False).agg({'Receita': 'sum', 'Quantidade' : 'sum'})
            dftop5 = df_grouby.sort_values(by='Quantidade',ascending=False).head(5)
            try:
                dados_html = []
                for index, linha in dftop5.iterrows():
                    dados_html.append({
                        "nome": linha['Produto'],
                        "quantidade": int(linha['Quantidade']),
                        "receita" : f"{linha['Receita']:,.2f}".replace(',','X').replace('.',',').replace('X','.')
                    })
                total_formatado = f"{faturamento:,.2f}".replace(',','X').replace('.',',').replace('X','.')
                return {
                    "titulo" : "Vendas",
                    "faturamento_total" : total_formatado,
                    "top_produtos" : dados_html
                }
            except Exception as g:
                logging.error(f"Ocorreu um erro ao processar os dados: {g}")
                return None
        except Exception as e:
            logging.error(f"Ocorreu um erro: {e}")
            return  None
    except FileExistsError as f:
        logging.error(f"Arquivo inexistente: {f}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format= '%(levelname)s : %(message)s')
    dados_falsos_do_pdf = [
        [
            ["Produto", "Quantidade", "Preco"],
            ["Teclado Mecanico", "10", "150,50"],
            ["Mouse Gamer", "20", "85,00"],
            ["Monitor", "5", "800,00"]
        ]
    ]
    if dados_falsos_do_pdf:
        resultado = processar(dados_falsos_do_pdf)
        print(resultado)