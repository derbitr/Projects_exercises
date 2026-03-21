import logging,datetime
from datetime import datetime, timedelta
import c1banco


def despesas(titulo: str, valor: float, categoria: str, data: str):
    try:
        logging.info("Iniciando conexão...")
        conexao = c1banco.conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO despesas (titulo,valor,categoria,data) VALUES (?,?,?,?)",(titulo,valor,categoria,data))
        conexao.commit()
        conexao.close()
        logging.info("Dados foram salvos na tabela")
    except Exception as f:
        logging.error(f"Erro ao iniciar : {f}")
        return
def filtrar_despesas(dias:int = 30):
    try:
        data_limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d");logging.info("Calculo das datas realizado")
        conexao = c1banco.conectar()
        if conexao:
            logging.info("Banco de dados conectado")
        else:
            logging.warning("Falha ao conectar ao banco de dados")
            return
        cursor = conexao.cursor()
        cursor.execute(""" SELECT * FROM despesas WHERE data >= ?""", (data_limite,))
        query = cursor.fetchall()
        conexao.close()
        return query
    except Exception as g:
        logging.error(f"Ocorreu um erro : {g}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format= '%(asctime)s : %(message)s ',  datefmt= '%H:%M:%S')
    data_agora = datetime.now().strftime('%Y-%m-%d')
    despesas("Almoço principal",50.00, "Alimentação", data_agora)
    lista_despesas = filtrar_despesas(40)
    logging.info(f"Despesas dos últimos 30 dias: {lista_despesas}")
    