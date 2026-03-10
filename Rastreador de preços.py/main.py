import logging
import gerenciador
import extractor
import csv

def config_sistema():
    logging.basicConfig(level=logging.INFO, format = '%(levelname)s: %(message)s')
def salvar_relatorio(dados : list,nome_ficheiro = "relatorio_precos.csv"):
    try:
        with open(nome_ficheiro, mode= 'w',newline= '', encoding= 'utf-8') as ficheiro:
            escrever = csv.writer(ficheiro)
            escrever.writerow(['Produto', 'Preço'])
            escrever.writerows(dados)
        logging.info(f"Relatorio armazenado : {nome_ficheiro}")
    except Exception as e:
        logging.error(f"Nenhum arquivo encontrado: {e}")

def iniciar_script():
    linha_alvo = gerenciador.ler_links("guardar_links.txt")
    if not linha_alvo:
        logging.warning(f"Nada para processar")
        return
    dados_salvar = []
    for linha in linha_alvo:
        titulo,preco = extractor.extrair_datas(linha)
        if titulo and preco:
            logging.info(f"Produto : {titulo} \nPreco : {preco} ")
            dados_salvar.append([titulo,preco])
        else:
            logging.warning(f"Nenhum produto encontrado")
    if dados_salvar:
        salvar_relatorio(dados_salvar)
        logging.info(f"Dados salvos")
if __name__ == "__main__":
    config_sistema()
    logging.info("Iniciando sistema")
    iniciar_script()
    
