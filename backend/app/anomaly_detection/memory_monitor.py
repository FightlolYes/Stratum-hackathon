import psutil
import asyncio

async def check_memory_anomaly(threshold=90):

    memory_usage = psutil.virtual_memory().percent
    return memory_usage
