import logging
import pdfplumber


def processador(caminho_pdf:str) -> list:
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            if pdf is None:
                logging.warning("Arquivo pdf vazio, escolha outro")
                return None
            for numero, pagina in enumerate(pdf.pages):
                tabela = pagina.extract_table()
                if tabela is not None:
                    logging.info("Tabela encontrada")
                    return tabela
            logging.warning("Tabela não encontrada")
            return []
    except FileNotFoundError as e:
        logging.error(f"Arquivo não encontrado: {e}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    resultado = processador(r"e:\Apostila Elevo Cursos - NR 11 - Operações com Empilhadeira.pdf")
    print(resultado)