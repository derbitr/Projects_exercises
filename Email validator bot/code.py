import pandas as pd
from email.message import EmailMessage; import os; import dotenv;import time;import smtplib;import logging



def config_logs():
    logging.basicConfig(
    filename='log_email.txt',
    level=logging.INFO,
    format="%(asctime)s\n%(levelname)s\n%(message)s"
)


def gerenciador_mensagem(rmt, n_cliente, email_cliente, vencimento):
    msg = EmailMessage()
    msg['Subject'] = "Aviso"
    msg['From'] = rmt
    msg['To'] = email_cliente
    msg.set_content(f"Ola, {n_cliente}, seu vencimento é no dia {vencimento}")
    return msg
                
def email():
    dotenv.load_dotenv()
    P_email = os.getenv("MEU_EMAIL")
    senha = os.getenv("SENHA_APP")
    try:
        clientes_tabela = pd.read_excel(r"e:\Downloads\Clientes.xlsx")
        print("Lendo tabela")
        time.sleep(0.7)
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
            s.login(P_email,senha)
            for indice,linha in clientes_tabela.iterrows():
                mensagem = gerenciador_mensagem(P_email,linha['Nome'],linha['Email'],linha['Vencimento'])
                
                try:
                    s.send_message(mensagem)
                    logging.info(f"Email enviado para : %s", mensagem['To'])
                    print(f"Email enviado com sucesso para : {linha['Nome']}")
                except Exception as erro:
                    print(f"Erro encontrado : {erro}")
                    logging.error("Erro encontrado: %s", erro)
    except Exception as e:
        print(f"Erro ao processar a tabela: {e}")
        logging.error("Falha ao processar : %s", e)
config_logs()
email()

    



