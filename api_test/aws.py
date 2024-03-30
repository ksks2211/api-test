import boto3
import json



session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name='ap-northeast-2'
)


# Use the client to retrieve the secret

def load_secret(secretId:str, key:str):    
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secretId)
    except Exception as e:
        print(e)
    else:
        # Decryption happens automatically using the SDKP
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            secret_dict = json.loads(secret)  # Convert the string to a dictionary                    
            if key in secret_dict: return secret_dict[key]
        else:
            # If the secret is a binary blob instead of a string, handle it here (not shown)
            pass
    return None            