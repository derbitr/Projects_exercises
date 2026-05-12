from pydantic import ValidationError
import yfinance,logging,m1banco,m2modelos
import pandas as pd







def config():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(message)s")
def capturar_dados(ticker,periodo="1mo"):
    try:
        dados = yfinance.download(tickers=ticker,period=periodo)
        if dados.empty:
            return []
        dados.columns = dados.columns.get_level_values(0)
        dados.reset_index(inplace=True)
        try:
            lista_tuplas = []
            for item in dados.itertuples():
                try:
                    m = m2modelos.ModeloBanco(Ano = item.Date.year,Ticker=ticker,Volume=item.Volume,
                                              Date=item.Date.strftime("%Y-%m-%d"),Open=item.Open,High=item.High,
                                              Low=item.Low,Close=item.Close)
                    if m:
                        logging.info("Tabelas criadas")
                        lista_tuplas.append(m.to_tuple())
                    else:
                        logging.warning("Falha ao criar")
                except ValidationError as e:
                    logging.error(f"Erro ocorrido: {e}")
            return lista_tuplas
        except Exception as g:
            logging.error(f"Erro ao iniciar varredura: {g}")
            return False
    except Exception as f:
        logging.error(f"Erro ao iniciar validação de dados: {f}")
        return False




