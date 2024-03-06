import psutil
import asyncio

async def check_cpu_anomaly(threshold=85, interval=1):

    cpu_usage = psutil.cpu_percent(interval=interval, percpu=False)
    return cpu_usage