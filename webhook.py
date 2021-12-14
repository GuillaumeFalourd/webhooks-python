import requests
import json

webhook_url = 'https://webhook.site/61a89a13-0f6d-4116-ae4d-95e4854683b3'

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