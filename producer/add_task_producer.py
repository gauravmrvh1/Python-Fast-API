import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        heartbeat=600,
        blocked_connection_timeout=300
    )
)

channel = connection.channel()

# Durable queue
channel.queue_declare(queue='gaurav_task_queue', durable=True)

message = "Gaurav Marvaha Task Data"

channel.basic_publish(
    exchange='',
    routing_key='gaurav_task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2  # make message persistent
    )
)

print("Message Sent")
connection.close()
