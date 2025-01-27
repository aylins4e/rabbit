from prometheus_client import start_http_server, Gauge
import requests
import time

# Prometheus metrics
RABBITMQ_QUEUE_MESSAGES = Gauge('rabbitmq_queue_messages', 'Number of messages in the queue')
RABBITMQ_CONNECTIONS = Gauge('rabbitmq_connections', 'Number of connections to RabbitMQ')

def fetch_rabbitmq_metrics():
    try:
        # Fetch metrics from RabbitMQ Prometheus endpoint
        response = requests.get('http://localhost:15692/metrics')
        metrics = response.text

        # Parse metrics (example: extract queue messages and connections)
        for line in metrics.split('\n'):
            if line.startswith('rabbitmq_queue_messages'):
                value = float(line.split(' ')[1])
                RABBITMQ_QUEUE_MESSAGES.set(value)
            elif line.startswith('rabbitmq_connections'):
                value = float(line.split(' ')[1])
                RABBITMQ_CONNECTIONS.set(value)
    except Exception as e:
        print(f"Error fetching RabbitMQ metrics: {e}")

if __name__ == '__main__':
    # Start Prometheus HTTP server
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")

    # Fetch and update metrics every 10 seconds
    while True:
        fetch_rabbitmq_metrics()
        time.sleep(10)