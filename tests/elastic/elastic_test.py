from api_test.elastic import client


search_query = {
    "query": {
        "match_all": {}
    }
}


res = client.search(index="blogposts", body=search_query)

print(res)

