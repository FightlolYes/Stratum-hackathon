from anomaly_detection.monitor import monitor_system
from anomaly_detection.anomaly_check import check_for_anomalies
import asyncio

async def main():
    while True:
        anomaly_detected = await check_for_anomalies()
        if anomaly_detected:
            print("Anomaly detected!")

if __name__ == "__main__":
    asyncio.run(main())
