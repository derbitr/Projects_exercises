import logging, jinja2
from jinja2 import Environment,FileSystemLoader

def construcao(dados: dict) -> bool:
    try:
        ambiente = Environment(loader=FileSystemLoader(r"E:\Usuário\Breno\codes\Projects_exercises\Pipeline BI"))
        template = ambiente.get_template("base.html")
        if not ambiente or not template:
            logging.warning("Dados indisponíveis")
            return None
        try:
            html = template.render(**dados)
            with open ("index.html","w",encoding="utf-8") as f:
                f.write(html)
                logging.info("Sistema gerado")
                return True
        except Exception as e:
            logging.error(f"Ocorreu um erro: {e}")
            return False
    except Exception as f:
        logging.error(f"Falha ao carregar dados: {f}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format= '%(levelname)s : %(message)s')
    dados_teste = {
        "titulo": "Dashboard de Teste",
        "faturamento_total": "1.000,00",
        "top_produtos": [{"nome": "Teste", "quantidade": 1, "receita": "1.000,00"}]
    }
    construcao(dados_teste)