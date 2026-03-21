import sqlite3, logging,os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

NOME_BANCO = os.path.join(DIRETORIO_ATUAL, "despesas.db")

def conectar():
    return sqlite3.connect(NOME_BANCO,check_same_thread=False)
def criar_tabela():
    logging.info("Iniciando conexão...")
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS despesas (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, valor REAL NOT NULL, categoria TEXT NOT NULL, data DATE NOT NULL)")
        conexao.commit()
        conexao.close()
        logging.info("Tabela verificada e criada")
    except Exception as e:
        logging.error(f"Falha ao carregar dados : {e}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= '%(levelname)s : %(message)s')
    criar_tabela()
