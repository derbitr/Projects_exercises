import json, os,logging


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PERGUNTAS = os.path.join(DIRETORIO_ATUAL,"banco_perguntas.json")
CAMINHO_PROGRESSO = os.path.join(DIRETORIO_ATUAL,"banco_respostas.json")
def carregar_progresso():
    logging.info("Iniciando sistema")
    if os.path.exists(CAMINHO_PROGRESSO):
        logging.info("Arquivo encontrado")
        with open(CAMINHO_PROGRESSO,'r',encoding='utf-8') as progresso:
            dados_progresso = json.load(progresso)
            return dados_progresso
    else:
        return {"pergunta" : "1" , "pontuacao" : 0}
def salvar_progresso(dados_progresso : dict):
    with open(CAMINHO_PROGRESSO,'w',encoding= 'utf-8') as save_progresso:
        json.dump(dados_progresso, save_progresso, indent=4)
        logging.info("Progresso salvo")
def carregar_perguntas():
    logging.info("Iniciando procura do arquivo json")
    if os.path.exists(CAMINHO_PERGUNTAS):
        logging.info("Arquivo encontrado, iniciando abertura")
        with open(CAMINHO_PERGUNTAS,'r',encoding='utf-8') as arquivo_perguntas:
            dados_perguntas = json.load(arquivo_perguntas)
            logging.info("Arquivos transformados")
            return dados_perguntas
    else:
        logging.warning("Arquivo não foi encontrado ou se encontra vazio")
        return {}
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= "%(levelname)s : %(message)s")
    simular_progresso = {"pergunta": "2", "pontuacao" : 10}
    salvar_progresso(simular_progresso)
    estado_salvo = carregar_progresso()
    print("Estado do jogo:", estado_salvo)
    resultado = carregar_perguntas()
    if resultado:
        print(resultado)
    else:
        logging.warning("Não foi acessar o quiz")
    

