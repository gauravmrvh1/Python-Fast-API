import pika
import json
import time

def send_email(email):
    print(f"Sending email to {email}...")
    time.sleep(5)  # simulate delay
    print("Email sent!")

def callback(ch, method, properties, body):
    data = json.loads(body)
    print("*************** Email Body *********************")
    print(data)
    try:
        send_email(data["email"])
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print("Error:", e)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)
channel = connection.channel()

channel.queue_declare(queue="email_queue", durable=True)
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="email_queue", on_message_callback=callback)

print("Waiting for messages...")
channel.start_consuming()
