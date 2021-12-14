import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

headers = {
    'Content-Type': 'application/json'
}

data = {
    'name': 'Guillaume',
    'phone': '+553499999-9999',
    'email': 'guillaume@test.com'
}

r = requests.post(
    url = webhook_url,
    headers = headers,
    data = json.dumps(data)
    )

if r.status_code == 200:
    print('Success')
else:
    print(r.status_code, r.content)