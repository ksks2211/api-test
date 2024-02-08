from elasticsearch import Elasticsearch
from .config import get_api_key


ES_ENDPOINT = get_api_key('ES_ENDPOINT')
ES_API_KEY=get_api_key('ES_API_KEY')

client = Elasticsearch(
  ES_ENDPOINT,
  api_key=ES_API_KEY,
  verify_certs=False
)