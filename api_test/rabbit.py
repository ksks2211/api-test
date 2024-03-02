import pika

from .config import get_api_key


RABBITMQ_HOST=get_api_key('RABBITMQ_HOST')
RABBITMQ_ID=get_api_key('RABBITMQ_ID')
RABBITMQ_PASSWORD=get_api_key('RABBITMQ_PASSWORD')
credentials = pika.PlainCredentials(RABBITMQ_ID, RABBITMQ_PASSWORD)



def get_blocking_conn(port=5672, virtual_host='/'):
  parameters= pika.ConnectionParameters(RABBITMQ_HOST,port,virtual_host,credentials)
  conn = pika.BlockingConnection(parameters)  
  return conn



  

  