from pydantic import ValidationError
import yfinance,logging,b1banco,b2modelos
import pandas as pd


def config():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(message)s")
def capturar_dados():
    dados_simulados = [
    {
        "Ano": 2024,
        "Data": "2024-05-10",
        "Nome": "Carlos Silva",
        "Altura": 1.85,
        "Cargo": "Engenheiro de Dados"
    },
    {
        "Ano": 2024,
        "Data": "2024-05-11",
        "Nome": "Ana Oliveira",
        "Altura": 1.68,
        "Cargo": "Cientista de Dados"
    },
    {
        "Ano": 1990,      
        "Data": "2024-05-12",
        "Nome": "Robô Errado",
        "Altura": 0.50,
        "Cargo": "QA"
    },
    {
        "Ano": 2024,
        "Data": "2024-05-13",
        "Nome": "Jo",      
        "Altura": 1.75,
        "Cargo": "Estagiário"
    },
    {
        "Ano": 2024,
        "Data": "2024-05-14",
        "Nome": "Gigante da Silva",
        "Altura": 4.20,   
        "Cargo": "Basquete"
    }]

    try:
        dados_tratados = []
        for dado in dados_simulados:
            try:
                b = b2modelos.ETLbanco(**dado)
                if b:
                    logging.info("Colunas criadas")
                    dados_tratados.append(b.to_tuple())
                else:
                    logging.warning("Falha")
            except ValidationError as e:
                logging.error(f"Erro ocorrido: {e}")
        return dados_tratados
    except Exception as g:
        logging.error(f"Erro: {g}")
        return False
    except Exception as h:
        logging.error(f"Erro: {h}")
        return False
if __name__ == "__main__":
    config()
    capturar_dados()
