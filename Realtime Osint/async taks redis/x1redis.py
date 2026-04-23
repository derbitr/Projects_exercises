from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os,redis
from urllib.parse import urlparse

from dotenv import load_dotenv
load_dotenv()

url = os.getenv("BASE_URL")
senha = os.getenv("REDIS_PASSWORD",0)
redisdb = os.getenv("REDIS_DB",None)


r = redis.ConnectionPool(
    host = url,
    port = 6379,
    password= senha,
    db = int(redisdb),
    decode_responses=True
    )
def get_redis():
    client = redis.Redis(connection_pool=r)
    try:
        client.ping()
    except redis.ConnectionError as e:
        raise e
    return client
