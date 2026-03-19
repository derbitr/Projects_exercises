import logging, pdfplumber



def extrair_tabela(caminho_pdf :str) -> list:
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            if pdf is None:
                logging.warning("Arquivo pdf não encontrado")
                return None
            for pagina in pdf.pages:
                tabela = pagina.extract_table()
                if tabela is not None:
                    logging.info("Tabela encontrada")
                    return tabela
            return []
    except Exception as e:
        logging.error(f"Erro encontrado: {e}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    teste = extrair_tabela(r"e:\Tópicos de Física - Vol. 2 - Termologia, Ondulatória e Óptica - 19ª ed - 2012.pdf")
    print(teste)
