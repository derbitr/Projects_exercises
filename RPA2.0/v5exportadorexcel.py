import pandas as pd, os,logging,v1banco,v2modelos,v3processadorpandas,v4watchdog
def config():
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")

def dados_excel(dados , nome_ficheiro_base):
    try:
        PASTA_RESULTADO = os.path.join(v1banco.DIRETORIO_ATUAL,"Relatório_gerais")
        if not os.path.exists(PASTA_RESULTADO):
            os.makedirs(PASTA_RESULTADO)
            logging.info("Pasta criada")
        df = pd.DataFrame(dados, columns=["Year","Region","Model","Units_Sold"])
        if not df.empty:
            nome_saida = nome_ficheiro_base.replace(".csv",".xlsx")
            nome_limpo = f"Relatório{nome_saida}"
            caminho_final = os.path.join(PASTA_RESULTADO,nome_limpo)
            df.to_excel(caminho_final,sheet_name="Vendas",index=False)
            logging.info("Excel criado")
            return True
    except Exception as h:
        logging.error(f"Erro encontrado: {h}")
        return False
if __name__ == "__main__":
    config()
    dados_excel([(2025, 'Global', 'X3', 500)], 'teste.csv')
    