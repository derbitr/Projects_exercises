import v1redis,v2modelos,v5logica
from v1redis import app

@app.task(bind = True, max_retries = 5)
def dados (self, modelo : v2modelos.ScrapperAlvo):
    lista = v2modelos.Scrapperresultado(
        url = modelo.url,
        task_id=self.request.id
    )
    try:
        logica = v5logica.ClientesWeb(modelo,lista)
        if logica:
            return lista
    except Exception as e:
        if str(e) == "Retry":
            raise self.retry(countdown = 60, exc = e)
        else:
            print(f"Erro não previsto : {e}")
            lista.sucesso = False
            lista.error = str(e)
            return lista
