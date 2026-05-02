import pandas as pd
import v1banco,v2modelos,logging


def config():
    logging.basicConfig(level=logging.INFO,format= "%(levelname)s:%(message)s")


def logica(caminho : str = r"E:\Usuário\Breno\codes\Projects_exercises\RPA2.0\bmw_global_sales_2018_2025.csv"):
    try:
        logging.info("Lendo ficheiro")
        ficheiro = pd.read_csv(caminho)
        if not ficheiro.empty:
            ficheiro_filtrado = ficheiro[["Year","Region","Model","Units_Sold"]].dropna()
            logging.info("Ficheiro filtrado")
            lista = []
            linhas_dict = ficheiro_filtrado.to_dict('records')
            for linha in linhas_dict:
                criar__modelo = v2modelos.ModeloTipo(**linha)
                if criar__modelo:
                    logging.info("Adicionado colunas filtrados na respectiva lista")
                    lista.append((criar__modelo.Year,criar__modelo.Region,criar__modelo.Model,criar__modelo.Units_Sold))
            return lista
    except Exception as e:
        logging.error(f"Falha ao acessar arquivo .csv: {e}")
        return False
if __name__ == "__main__":
    config()
    logging.info("registro de logs iniciado")
    print(logica())