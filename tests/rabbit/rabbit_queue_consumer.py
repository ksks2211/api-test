from api_test.rabbit import get_blocking_conn

def callback(ch, method, properties, body:bytes):
    print(f" [x] Received {body.decode('utf-8')}")



# Connect to RabbitMQ server
connection = get_blocking_conn()
channel = connection.channel()

# Declare the queue to ensure it exists.
channel.queue_declare(queue='hello')

# Subscribe to the queue
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
