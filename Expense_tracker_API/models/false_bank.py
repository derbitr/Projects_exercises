from core.logs import iniciar_log
logger = iniciar_log("Banco de dados")


banco_teste = {"email" : {"id" : 1, "email" : "email_1@teste.com",
                         "senha": "senha_hash"}}

banco_teste = {}
def buscar_email(email:str):
    logger.info("Iniciando busca de falso banco de dados")
    if email in banco_teste:
        return banco_teste[email]
    else:
        return None
def receber_usuario(dados_usuario):
    try:
        logger.info("Iniciando salvamento de usuário")
        email_recebido = dados_usuario["email"]
        dados_usuario["id"] = len(banco_teste) + 1
        banco_teste[email_recebido] = dados_usuario
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return None
if __name__ == "__main__":
    receber_usuario()
    buscar_email()