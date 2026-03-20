import os, logging, shutil

def organizar_arquivo(caminho_origem:str,cofre:str,categoria:str) -> bool:
    try:
        pasta_alvo = os.path.join(cofre,categoria)
        logging.info("Acessando pasta")
        try:
            if pasta_alvo:
                os.makedirs(pasta_alvo, exist_ok=True)
                nome_arquivo = os.path.basename(caminho_origem)
                caminho_destino = os.path.join(pasta_alvo,nome_arquivo)
                shutil.move(caminho_origem,caminho_destino)
                return True
            else:
                logging.warning("Não foi possivel realizar a operação")
                return False
        except Exception as f:
            logging.error(f"Falha ao carregar os dados: {f}")
            return None
    except FileExistsError as g:
        logging.error(f"Arquivo inexistente : {g}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format= '%(levelname)s : %(message)s')
    arquivo_teste = "teste.txt"
    pasta_cofre = "Cofre_Organizado"
    categoria_teste = "Documentos"
    if os.path.exists(arquivo_teste):
        organizar_arquivo(arquivo_teste,pasta_cofre,categoria_teste)
