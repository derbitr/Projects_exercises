from openpyxl import Workbook
from openpyxl.styles import Font
import logging

def comparar(lista_livras : list, nome_arquivo:str = "Comparador.xlsx"):
    cabecalho = ["Título do Livro", "Preço (£)", "Link"]
    if not lista_livras or not nome_arquivo:
        logging.warning("Dados não encontrados")
        return
    try:
        livro = Workbook()
        folha = livro.active
        folha.title = "Comparação"
        folha.append(cabecalho)
        for cor in folha[1]:
            cor.font = Font(bold=True)
        for item in lista_livras:
            linha = [item["titulo"], item["preco"], item["link"]]
            folha.append(linha)
        livro.save(nome_arquivo)
        logging.info("Arquivo excel gerado")
    except Exception as e:
        logging.error(f"Erro ao acessar o arquivo: {e}")
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    teste = [
        {"titulo": "Livro Falso 1", "preco": 25.99, "link": "http://site.com/1"},
        {"titulo": "Livro Falso 2", "preco": 14.50, "link": "http://site.com/2"}
    ]
    comparar(teste)

    
