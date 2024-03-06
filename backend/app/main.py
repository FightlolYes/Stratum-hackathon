from anomaly_detection.monitor import monitor_system
import asyncio

if __name__ == "__main__":
    asyncio.run(monitor_system())