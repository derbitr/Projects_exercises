from celery import Celery
from core.config import settings

app = Celery("scraper_pedreiro",set_as_current = True,backend=settings.REDIS_URL,broker=settings.REDIS_URL,include=['worker.tasks'])
app.conf.update(
    timezone="America/Sao_Paulo",
    enable_utc = True
)

