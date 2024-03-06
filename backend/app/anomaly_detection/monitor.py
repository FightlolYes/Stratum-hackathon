import asyncio
from .cpu_monitor import check_cpu_anomaly
from .memory_monitor import check_memory_anomaly
from .disk_monitor import check_disk_usage

async def monitor_system():
    while True:
        cpu_usage = await check_cpu_anomaly()
        memory_usage = await check_memory_anomaly()
        disk_usage = check_disk_usage()

        print(f"CPU usage: {cpu_usage}")
        print(f"Memory usage: {memory_usage}")
        print(f"Disk usage: {disk_usage}")
        
        await asyncio.sleep(2)
