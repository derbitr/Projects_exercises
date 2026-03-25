import os, logging,sqlite3
from datetime import datetime, timedelta

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
NOME_BANCO =os.path.join(DIRETORIO_ATUAL, "backup_rpa.db")

def conectar():
    return sqlite3.connect(NOME_BANCO,check_same_thread=False)
def tabela():
    logging.info("Iniciando acesso ao banco de dados")
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS despesas_locais( id INTEGER PRIMARY KEY AUTOINCREMENT, valor REAL, categoria TEXT, data TEXT)")
        conexao.commit()
        conexao.close()
        logging.info("Tabela verificada e criada")
    except Exception as e:
        logging.error(f"Falha ao iniciar: {e}")
        return
def inserir_dados(valor: float,categoria :str , data: str):
    try:
        logging.info("Iniciando processo de inserção de dados no banco de dados...")
        conexao_dados = conectar()
        cursor_dados = conexao_dados.cursor()
        cursor_dados.execute("INSERT INTO despesas_locais(valor,categoria,data) VALUES (?,?,?)",(valor,categoria,data))
        conexao_dados.commit()
        conexao_dados.close()
        logging.info("Dados inseridos no banco de dados")
    except Exception as f:
        logging.error(f"Falha na tentativa de inserção de dados: {f}")
        return
def contar_dias(dias:int = 30):
    try:
        data_limite =(datetime.now() - (timedelta(days=dias))).strftime("%Y-%m-%d")
        logging.info("Processo de filtro de dias realizado")
        conexao = conectar()
        if conexao:
            logging.info("Banco de dados conectado")
        else:
            logging.warning("Falha ao conectar ao banco de dados")
            return
        cursor = conexao.cursor()
        cursor.execute("""SELECT * FROM despesas_locais WHERE data >= ?""",(data_limite,))
        query = cursor.fetchall()
        if query:
            return query
        else:
            logging.warning("Falha ao selecionar dados")
    except Exception as hg:
        logging.error(f"Erro: {hg}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= "%(asctime)s : %(message)s",datefmt= "%H:%M:%S")
    conectar()
    data_agora = datetime.now().strftime('%Y-%m-%d')
    tabela()
    inserir_dados(400,"Produtos",data_agora)
    lista = contar_dias(30)
    logging.info(f"Despesas dos últimos 30 dias: {lista}")
