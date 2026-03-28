from openpyxl import Workbook
from openpyxl.styles import Font
import logging

def relatorio(dados : list,nome_planilha: str= "RelatorioPrecos_excel.xlsx"):
    cabeçalho =["Link produto: ","Preco USD: ", "Preco convertido: ", "Cotação dólar: "]
    if not nome_planilha or not dados:
        logging.warning("Valores inexistentes")
        return
    try:
        livro = Workbook()
        folha = livro.active
        folha.title = "Items"
        folha.append(cabeçalho)
        for n in folha[1]:
            n.font = Font(bold=True)
        for l in dados:
            folha.append(l)
        livro.save(nome_planilha)
    except Exception as e:
        logging.error(f"Erro ao processr dados: {e}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    teste = [
        ["amazon.com/dp/B0741X82H1", 69.99, 350.00, 5.00],
        ["amazon.com/dp/B08F7PTF53", 199.50, 997.50, 5.00]
    ]
    logging.info("Iniciando...")
    relatorio(teste)