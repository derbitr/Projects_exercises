import os, logging, sqlite3, requests,json
import pandas as pd
from datetime import datetime, timedelta


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_ATUAL = os.path.join(DIRETORIO_ATUAL,"Etl_banco.db")


def config_log():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s: %(message)s")
    return "Registros de informação criado"
def banco():
    return sqlite3.connect(PASTA_ATUAL,check_same_thread=False)
def criar_tabela():
    logging.info("Iniciando criação de tabela")
    try:
        conexao = banco()
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS financeiro(ano INTEGER, ticker TEXT ,volume INTEGER, date TEXT, open REAL, high REAL, low REAL, close REAL, UNIQUE(ticker,date) )")
        conexao.commit()
        conexao.close()
        logging.info("Tabela criada")
    except Exception as e:
        logging.error(f"Ocorreu um erro; {e}")
        return
def inserir_dados(dados):
    logging.info("Iniciando inserção de dados")
    try:
        conexao = banco()
        cursor = conexao.cursor()
        cursor.executemany("INSERT OR IGNORE INTO financeiro(ano,ticker,volume,date,open,high,low,close) VALUES (?,?,?,?,?,?,?,?)",dados)
        conexao.commit()
        conexao.close()
        logging.info("Dados inseridos")
    except Exception as f:
        logging.error(f"Erro ao inserir dados: {f}")
        return
def contar_ano(ano : int = 1):
    resultado = []
    try:
        ano_limite = datetime.now().year - ano
        logging.info("Filtro de ano realizado")
        conexao = banco()
        if conexao:
            logging.info("Banco conectado")
        else:
            logging.warning("Falha ao conectar o banco de dados")
            return
        cursor = conexao.cursor()
        cursor.execute("""SELECT * FROM financeiro WHERE ano >= ?""",(ano_limite,))
        resultado = cursor.fetchall()
    except Exception as g:
        logging.error(f"Falha ao filtrar: {g}")
    return resultado
def enviar_para_nuvem(dados):
    url = "https://api.de_mentira.com/vendas" #Apenas para testar lógica de enviar dados via requests, função fantasma
    try:
        payload = []
        for item in dados:
            payload.append({
                "ano":item[0],
                "ticker":item[1],
                "volume":item[2],
                "date":item[3],
                "open":item[4],
                "high":item[5],
                "low":item[6],
                "close":item[7]
                    })
        r = requests.post(url=url,json=payload,timeout=5)
        if r.status_code in [200,201]:
            logging.info("Operação foi um sucesso")
            return True
        else:
            logging.error("Erro na operação")
    except Exception as g:
        logging.error(F"Falha ao tratar dados: {g}")
        return False
if __name__ == "__main__":
    config_log()
    banco()
    data = [(2020,"AASC",100,"2020-05-25",10.5,15.0,8.0,5.0)]
    inserir_dados(data)
    resultado = contar_ano(1)
    logging.info(f"resultado: {resultado}")
    enviar_para_nuvem(data)