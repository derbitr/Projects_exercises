import pandas as pd, os ,logging,c2banco,main,c1sentinela
def config():
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")
def dados_excel():
    try:
        diretorio = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(diretorio,"relatorio_fechamento.xlsx")
        if not caminho:
            logging.warning("Falha ao acessar diretorio")
            return
    except Exception as e:
        logging.error(f"Erro: {e}")
        return
def relatorio():
    dias = c2banco.contar_dias(30)
    if not dias:
        logging.warning("Banco de dados vazio")
        return
    df = pd.DataFrame(dias,columns=["ID","Valor","Categoria","Data"])
    resumo = df.groupby("Categoria")["Valor"].sum()
    with pd.ExcelWriter("relatorio_fechamento.xlsx",engine="openpyxl") as excel:
        df.to_excel(excel,sheet_name="Resumo Categoria")
        logging.info("Relatório gerado")
if __name__ == "__main__":
    config()
    dados_excel()
    relatorio()