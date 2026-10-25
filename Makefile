.PHONY: test lint build run clean

test:
	pytest tests/ -v

lint:
	flake8 src/ tests/ --max-line-length=100

build:
	docker build -t netmetrics/telemetry-agent:latest .

run:
	docker compose up -d

clean:
	rm -rf __pycache__ .pytest_cache/ *.log
