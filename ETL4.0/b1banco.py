import os, logging,sqlite3,requests,json
import pandas as pd
from datetime import datetime,timedelta

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_ATUAL = os.path.join(DIRETORIO_ATUAL,"Etl4banco.db")


def config_log():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(message)s")
    return "Log iniciado"
def banco():
    return sqlite3.connect(PASTA_ATUAL,check_same_thread=False)
def criar_tabela():
    logging.info("Criando tabela no banco de dados")
    try:
        conexao = banco()
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS informacoes(ano INTEGER, data TEXT, nome TEXT, altura FLOAT, cargo TEXT)")
        conexao.commit()
        conexao.close()
        logging.info("Tabela criada")
    except Exception as e:
        logging.error(F"Falha ao criar banco: {e}")
        return
def inserir_dados(dados):
    logging.info("Iniciando inserção de dados")
    try:
        conexao = banco()
        cursor = conexao.cursor()
        cursor.executemany("INSERT OR IGNORE INTO informacoes(ano,data,nome,altura,cargo) VALUES (?,?,?,?,?)",dados)
        conexao.commit()
        conexao.close()
        logging.info("Dados inseridos")
    except Exception as g:
        logging.error(f"Falha ao inserir dados: {g}")
        return
def contar_ano(ano:int = 1):
    resultado = []
    try:
        ano_limite = datetime.now().year - ano
        logging.info("Filtro realizado")
        conexao = banco()
        if conexao:
            logging.info("Banco conectado")
        else:
            logging.warning("Falha ao conectar banco")
            return
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM informacoes WHERE ano >= ? ",(ano_limite,))
        resultado = cursor.fetchall()
    except Exception as h:
        logging.error(f"Falha: {h}")
    return resultado
def enviar_nuvem(dados):
    url = "api_de_mentiririnha.com/Informações" #Novamente outra url de mentira apenas para testar a lógica da criação do banco de dados
    try:
        payload = []
        for item in dados:
            payload.append({
                "ano":item[0],
                "data":item[1],
                "nome":item[2],
                "altura":item[3],
                "cargo":item[4]
            })
        r = requests.post(url=url,json=payload,timeout=5)
        if r.status_code in [200,201]:
            logging.info("Sucesso")
            return True
        else:
            logging.error("Erro")
    except Exception as k:
        logging.error(f"Ocorreu um erro: {k}")
        return False
if __name__ == "__main__":
    config_log()
    banco()
    criar_tabela()
    data = [(2026,"15-05-2026","Breno Luiz",1.71,"Estudante")]
    inserir_dados(data)
    resultado = contar_ano(1)
    logging.info(F"Resultado: {resultado}")
    enviar_nuvem(data)