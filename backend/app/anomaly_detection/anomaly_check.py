import asyncio
from .cpu_monitor import check_cpu_anomaly
from .memory_monitor import check_memory_anomaly
from .disk_monitor import check_disk_usage

async def check_for_anomalies(CPU_THRESHOLD=85, MEMORY_THRESHOLD=90, DISK_THRESHOLD=85):
        cpu_usage = await check_cpu_anomaly()
        memory_usage = await check_memory_anomaly()
        disk_usage = await check_disk_usage()

        print(f"Checking for anomalies...")
        if cpu_usage > CPU_THRESHOLD:
            return True
        
        if memory_usage > MEMORY_THRESHOLD:
            return True
        
        if disk_usage > DISK_THRESHOLD:
            return True

        await asyncio.sleep(2)