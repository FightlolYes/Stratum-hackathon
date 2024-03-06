import psutil

async def check_disk_usage(partition='/'):
    disk_usage = psutil.disk_usage(partition)
    return disk_usage.percent