import os, logging, sqlite3, requests,json
import pandas as pd
from datetime import datetime, timedelta

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_ATUAL = os.path.join(DIRETORIO_ATUAL,"RPA.db")

def config_log():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s : %(message)s")
    return "Registros de informações iniciado"
def banco():
    return sqlite3.connect(PASTA_ATUAL, check_same_thread=False)
def criar_tabela():
    logging.info("Iniciando acesso ao banco de dados")
    try:
        conexao = banco()
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS principais (year INTEGER, region TEXT, model TEXT, unidades_vendidas INT)")
        conexao.commit()
        conexao.close()
        logging.info("Tabela criada")
    except Exception as g:
        logging.error(f"Ocorreu um erro: {g}")
        return
def inserir_dados(dados):
    logging.info("Iniciando inserção de dados selecionados")
    try:
        conexao = banco()
        cursor = conexao.cursor()
        cursor.executemany("INSERT INTO principais(year, region, model, unidades_vendidas) VALUES (?,?,?,?)",dados)
        conexao.commit()
        conexao.close()
        logging.info("Dados inseridos na tabela")
        return True
    except Exception as e:
        logging.error(f"Erro ao inserir dados: {e}")
        return
def contar_dias(ano : int = 10):
    try:
        ano_limite = datetime.now().year - ano
        logging.info("Filtro de ano realizado")
        conexao = banco()
        if conexao:
            logging.info("Banco conectado")
        else:
            logging.warning("Banco não conectado")
            return
        cursor = conexao.cursor()
        cursor.execute( """ SELECT * FROM principais WHERE year >= ?""",(ano_limite,) )
        resultado = cursor.fetchall()
        return resultado
    except Exception as h:
        logging.error(f"Erro encontrado: {h}")
        return
def enviar_nuvem(dados):
    url = "https://api.empresa.com/vendas" #Url Fictícia, apenas para testes do try/except
    try:
        payload = []
        for item in dados:
            payload.append({
                "year": item[0],
                "region": item[1],
                "model": item[2],
                "unidades_vendidas": item[3]
            })
        r = requests.post(url=url,json=payload,timeout=5)
        if r.status_code in [200,201]:
            logging.info("Operação foi um sucesso")
            return True
        else:
            logging.error("Erro na operação")
    except Exception as j:
        logging.error(f"Erro ao tratar dados: {j}")
        return False
if __name__ == "__main__":
    config_log()
    criar_tabela()
    dados = [(2025,"Europe","X5",150),
        (2025,"China","i4",260)]
    inserir_dados(dados)
    resultado = contar_dias(2)
    print(f"dados: {resultado}")
    enviar_nuvem(dados)