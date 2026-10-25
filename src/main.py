import asyncio
import logging
import sys
from src.collector import SystemMetricsCollector
from src.transmitter import TelemetryTransmitter

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger("telemetry-agent")

async def main():
    logger.info("Initializing NetMetrics Telemetry Relay Agent v2.4.1...")
    collector = SystemMetricsCollector()
    transmitter = TelemetryTransmitter()

    logger.info("Starting telemetry harvest loop (interval: 15s)...")
    try:
        while True:
            metrics = await collector.collect_metrics()
            logger.info("Harvested telemetry frame: cpu=%.1f%%, mem=%.1f%%, net_io=%d pkts",
                        metrics["cpu_utilization"], metrics["memory_utilization"], metrics["packets_tx"])
            await transmitter.transmit(metrics)
            await asyncio.sleep(15)
    except (KeyboardInterrupt, asyncio.CancelledError):
        logger.info("Shutdown signal received. Flushing buffers...")
    finally:
        await transmitter.close()
        logger.info("Telemetry agent stopped cleanly.")

if __name__ == "__main__":
    asyncio.run(main())
