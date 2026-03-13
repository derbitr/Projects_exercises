import logging; import motor_excel; import dados

def config():
    logging.basicConfig(level=logging.INFO,format= '%(levelname)s: %(message)s')
def start():
    vendas = dados.obter_dados()
    if not vendas:
        logging.error("Erro, lista vazia")
        return
    motor_excel.relatorio(vendas)
if __name__ == "__main__":
    config()
    logging.info("Inicializando")
    start()
