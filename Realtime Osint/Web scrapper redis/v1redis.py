from celery import Celery
import os,redis
from dotenv import load_dotenv
load_dotenv()

url_base = os.getenv("BASE_URL")
backend_url = os.getenv("BACK_URL")




app = Celery(
    "scrapper_bot",
    broker=url_base,
    backend=backend_url
)

app.conf.update(
    task_serializer = "json",
    accept_content = ["json"],
    result_serializer = "json",
    timezone = "UTC",
    enable_utc = True,
    task_acks_late = True,
    worker_prefetch_multiplier = 1
    )