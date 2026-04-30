import os
from broadcaster import Broadcast

redis_url = os.getenv("REDIS_URL","redis://localhost:6379/1")


broadcast = Broadcast(redis_url)

async def iniciar():
    await broadcast.connect()
async def desligar():
    await broadcast.disconnect()