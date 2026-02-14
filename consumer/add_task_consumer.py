import pika, time


def start_task_consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()
    channel.queue_declare(queue='gaurav_task_queue', durable=True)

    def callback(ch, method, properties, body):
        print("Received:", body.decode())
        time.sleep(15)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue='gaurav_task_queue',
        on_message_callback=callback
    )

    print("Waiting for messages task consumer ......")
    channel.start_consuming()
