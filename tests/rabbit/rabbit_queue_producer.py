from api_test.rabbit import get_blocking_conn

connection = get_blocking_conn()
channel = connection.channel()


channel.queue_declare(queue='hello')


channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")


connection.close()
