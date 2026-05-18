from worker.celery_app import app
from core.logs import registro
import time,httpx
from bs4 import BeautifulSoup


logger = registro("CELERY_TASK")

@app.task
def pegar_dados(url_site : str):
    logger.info(f"Busca de dados iniciada em: {url_site}")
    try:
        titulo = "Sem título"
        headers = {"User-Agent":"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"}
        with httpx.Client(headers=headers,follow_redirects=True) as cliente:
            resposta = cliente.get(url_site)
            if resposta.status_code in [200,201]:
                soup = BeautifulSoup(resposta.text, "html.parser")
                titulo = soup.title.string if soup.title else "Sem título"
        logger.info(f"Busca de dados concluída: {url_site}")
        return {"site": url_site, "status": "concluído", "dados": {"pagina": titulo.strip()}}
    except Exception as k:
        logger.error(f"Ocorreu um erro: {k}")
        return{"site": url_site, "status": "erro", "motivo": str(k)}