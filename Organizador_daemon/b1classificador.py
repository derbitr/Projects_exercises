import os,logging


def leitor_arquivos(nome_arquivo:str)->str:
    try:
        nome,extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()
        match extensao:
            case ".pdf"|".doc"|".docx"|".txt":
                logging.info("Separando documentos...")
                return "Documentos"
            case ".jpg"|".jpeg"|".png"|".gif":
                logging.info("Separando imagens..")
                return "Imagens"
            case _:
                logging.info("Separando arquivos diversos")
                return "Outros"
    except Exception as e:
        logging.error(f"Ocorreu um erro ao buscar arquivo: {e}")
        return None
if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    teste = "fatura_internet.pdf"
    if teste:
        print(leitor_arquivos(teste))