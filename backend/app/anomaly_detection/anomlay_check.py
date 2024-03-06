import asyncio
from .cpu_monitor import check_cpu_anomaly
from .memory_monitor import check_memory_anomaly
from .disk_monitor import check_disk_usage

async def check_for_anomalies(CPU_THRESHOLD=85, MEMORY_THRESHOLD=90, DISK_THRESHOLD=85):
    while True:
        cpu_usage = await check_cpu_anomaly()
        memory_usage = await check_memory_anomaly()
        disk_usage = check_disk_usage()

        if cpu_usage > CPU_THRESHOLD:
            print(f"High CPU usage: {cpu_usage}")
        if memory_usage > MEMORY_THRESHOLD:
            print(f"High memory usage: {memory_usage}")
        if disk_usage > DISK_THRESHOLD:
            print(f"High disk usage: {disk_usage}")

        await asyncio.sleep(2)