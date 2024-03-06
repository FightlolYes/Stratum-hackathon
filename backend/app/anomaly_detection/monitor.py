import asyncio
from .cpu_monitor import check_cpu_anomaly
from .memory_monitor import check_memory_anomaly

async def monitor_system():
    while True:
        cpu_anomaly = await check_cpu_anomaly()
        memory_anomaly = await check_memory_anomaly()

        if cpu_anomaly:
            print("CPU usage anomaly detected.")
        if memory_anomaly:
            print("Memory usage anomaly detected.")
        
        await asyncio.sleep(60)
