import pytest
import asyncio
from src.collector import SystemMetricsCollector

def test_metrics_collection():
    collector = SystemMetricsCollector()
    data = asyncio.run(collector.collect_metrics())
    assert "cpu_utilization" in data
    assert data["status"] == "healthy"
