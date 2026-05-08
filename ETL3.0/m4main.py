import m1banco,m2modelos,m3extrator, logging

def iniciar():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s: %(message)s")
    logging.info("Sistema iniciado")
    m1banco.criar_tabela()
    lista_alvo = ["AAPL","TSLA","PETR4.SA","BTC-USD"]
    for ticker in lista_alvo:
        try:
            lista_tuplas = m3extrator.capturar_dados(ticker)
            if lista_tuplas:
                logging.info("Enviando dados para o banco de dados")
                m1banco.inserir_dados(lista_tuplas)
                logging.info(f"Dado salvo: {ticker}")
                pass
            else:
                logging.warning(f"Sem dado para : {ticker}")
                continue
        except Exception as e:
            logging.error(F"Falha ao capturar dados: {e}")
            continue
    logging.info("Processo finalizado")
if __name__ == "__main__":
    iniciar() 