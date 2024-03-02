
from api_test.rabbit import get_blocking_conn



# Connect to RabbitMQ server
connection = get_blocking_conn()
channel = connection.channel()





# Declare a fanout exchange
exchange_name = 'logs'
channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

# Publish a message to the exchange
message = "info: Hello World!"
channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
print(f" [x] Sent {message}")

# Close the connection
connection.close()
