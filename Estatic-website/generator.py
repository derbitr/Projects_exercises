import jinja2, logging
from jinja2 import Environment,FileSystemLoader

def construção(dados: dict):
    try:
        ambiente = Environment(loader=FileSystemLoader(r"Projects_exercises\Estatic-website"))
        template = ambiente.get_template("base.html")
        if not ambiente or not template:
            logging.warning("Dados indisponíveis")
            return None
        try:
            html = template.render(**dados)
            with open ("index.html", "w",encoding= 'utf-8') as f:
                f.write(html)
        except Exception as e:
            logging.error(f"Erro ao escriçao no arquivo: {e}")
            return None
    except Exception as g:
        logging.error(f"Erro ao procurar arquivo: {g}")
        return None
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format = '%(levelname)s : %(message)s')
    dados_vendas = {
        "pagina_titulo": "Dashboard de Vendas Automático",
        "faturamento": "45.200,00",
        "produtos_destaque": [
            {"nome": "Notebook Pro", "qtd": 15},
            {"nome": "Teclado Mecânico", "qtd": 42},
            {"nome": "Monitor Ultrawide", "qtd": 8}
        ]
    }
    construção(dados_vendas)
