import pika
import json

def publish_email_message(message: dict):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        channel = connection.channel()

        channel.queue_declare(queue="email_queue", durable=True)

        channel.basic_publish(
            exchange="",
            routing_key="email_queue",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2  # persistent
            ),
        )

        connection.close()
        
    except Exception as e:
        print("Email publish error:", e)
