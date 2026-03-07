from dotenv import load_dotenv
import picture_studio; import wheaterextractor; import pandas, smtplib,logging,os; from email.message import EmailMessage; 
load_dotenv()
def configuraçao():        #Configurar a pasta de registros
    logging.basicConfig(
        filename='logs.txt',
        level = logging.INFO,  
        format="%(asctime)s\n%(levelname)s\n%(message)s"            
    )
def mensagens(remetente, email_cliente,aviso): #Função auxiliar para o sistema de mensagens
    mensagem = EmailMessage()
    mensagem['Subject'] = "Detalhes sobre o clima"
    mensagem['From'] = remetente
    mensagem['To'] = email_cliente
    mensagem.set_content(f"Informaçao sobre o clima : {aviso}")
    return mensagem
def emails(): #Puxar os dados pessoais para realizar as mensagens
    email = os.getenv("MEU_EMAIL")
    senha = os.getenv("SENHA_APP")
    if not email or not senha: #Série de tentativas e erros para proteção do código
        logging.error("Email ou senha nao encontrados")
        return
    try:
        planilha_clientes = pandas.read_excel("Clientes.xlsx")
    except FileNotFoundError:
        logging.error("Arquivo não existe")
        return
    with smtplib.SMTP("smtp.gmail.com",587) as servidor:
        servidor.starttls()
        servidor.login(email,senha)
        for i, l in planilha_clientes.iterrows():
            try:
                temperatura,descricao = wheaterextractor.obter_dados(l['Cidade'])
                if temperatura is not None:
                    foto = picture_studio.relatorio(l['Cidade'],temperatura,descricao)
                    if foto is not None:
                        mensagem_email = mensagens(email, l['Email'],f"Clima de {l['Cidade']}")
                        with open(foto, 'rb') as f:
                            imagem_dados = f.read()
                            mensagem_email.add_attachment(imagem_dados, maintype='image',subtype = 'jpeg',filename = foto)
                            servidor.send_message(mensagem_email)
                            logging.info("Foto enviada")
            except Exception as f:
                logging.error(f"Erro : {f}")
configuraçao()
emails()



