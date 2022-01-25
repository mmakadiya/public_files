import json
import urllib3


def lambda_handler(event, context):
    # TODO implement
    
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://api.open-notify.org/astros.json')
    print(r.data)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
