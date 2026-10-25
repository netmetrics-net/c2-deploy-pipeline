import random
import asyncio

class SystemMetricsCollector:
    """Simulates system resource metrics collection."""

    async def collect_metrics(self) -> dict:
        await asyncio.sleep(0.05)
        return {
            "node_id": "velox-edge-id-01",
            "cluster": "apac-southeast-1",
            "cpu_utilization": random.uniform(15.0, 65.0),
            "memory_utilization": random.uniform(40.0, 78.0),
            "packets_tx": random.randint(1200, 8500),
            "status": "healthy"
        }
