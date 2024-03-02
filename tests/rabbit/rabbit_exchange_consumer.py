from api_test.rabbit import get_blocking_conn

connection = get_blocking_conn()
channel = connection.channel()

def callback(ch, method, properties, body:bytes):
    print(f" [x] Received {body.decode('utf-8')}")


# Declare a fanout exchange
exchange_name = 'logs'
channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

# Declare a queue with a generated name
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the exchange
channel.queue_bind(exchange=exchange_name, queue=queue_name)

# Subscribe to the queue
channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
