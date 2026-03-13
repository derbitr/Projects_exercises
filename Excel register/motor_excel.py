from openpyxl import Workbook; from openpyxl.styles import Font
import logging


def relatorio(dados: list, nome_planilha : str= "Relatorio_excel.xlsx"):
    if not dados or not nome_planilha:
        logging.warning("Valores vazios")
        return
    try:
        livro = Workbook()
        folha = livro.active
        folha.title= "Vendas"
        negrito = ["Produto","Quantidade","Preço Unitário","Total"]
        folha.append(negrito)
        for n in folha[1]:
            n.font = Font(bold=True)
        for linha in dados:
            folha.append(linha)
        livro.save(nome_planilha)
        logging.info(f"Sucesso, planilha salva: {nome_planilha}")
    except PermissionError as e:
        logging.error(f"Erro detectado: {e}")
    except Exception as f:
        logging.error(f"Erro : {f}")
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dados_testes = [
        ["Teclado",5,80,800,400],
        ["Mouse", 50,900,600],
        ["Monitor",400,600,500,400]
    ]
    if dados_testes:
        relatorio(dados_testes)