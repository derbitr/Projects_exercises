import json, os,logging

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PERGUNTAS = os.path.join(DIRETORIO_ATUAL,"perguntas.json")
CAMINHO_PROGRESSO = os.path.join(DIRETORIO_ATUAL,"progresso.json")
def carregar_progresso():
    logging.info("Iniciando sistema de salvamento de progresso")
    if os.path.exists(CAMINHO_PROGRESSO):
        logging.info("Arquivo encontrado")
        with open(CAMINHO_PROGRESSO,'r',encoding='utf-8') as progresso:
            dados_progresso = json.load(progresso)
            return dados_progresso
    else:
        return {"pergunta_atual" : "1", "pontuacao" : 0}
def salvar_progresso(dados_progresso: dict):
    with open(CAMINHO_PROGRESSO, 'w',encoding='utf-8') as save_progresso:
        json.dump(dados_progresso,save_progresso,indent=4)
        logging.info("Progresso salvo")
def carregar_perguntas():
    logging.info("Iniciando procura do arquivo json com as perguntas")
    if os.path.exists(CAMINHO_PERGUNTAS):
        logging.info("Arquivo encontrado, iniciando abertura")
        with open(CAMINHO_PERGUNTAS,'r',encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            logging.info("Arquivos transformados")
            return dados
    else:
        logging.warning("Arquivo nao foi encontrado ou se encontra vazio")
        return {}
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= "%(levelname)s : %(message)s")
    progresso_simulado = {"pergunta_atual": "2", "pontuacao": 10}
    salvar_progresso(progresso_simulado)
    estado_salvo = carregar_progresso()
    print("Estado do Jogo:", estado_salvo)
    resultado = carregar_perguntas()
    if resultado:
        print(resultado)
    else:
        logging.warning("Não foi possível iniciar")
    

