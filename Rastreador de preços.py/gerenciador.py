import logging


def ler_links(caminho_arquivo : str ) -> list:
    if not caminho_arquivo or not caminho_arquivo.strip():
        return []
    try:
        with open(caminho_arquivo, 'r',encoding = 'utf-8') as arquivo:
            link_limpo = set()
            for linha in arquivo:
                link = linha.strip()
                if link and link.startswith("http"):
                    link_limpo.add(link)
                elif link:
                    logging.warning(f"Linha ignorada: {link}")
            return list(link_limpo)
    except FileNotFoundError:
        logging.error(f"O arquivo {caminho_arquivo} não foi encontrado")
        return []
    except Exception as e:
        logging.error(f"Erro encontrado: {e}")
        return []
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    links = ler_links("guardar_links.txt")
    print(f"Links guardados : {links}")