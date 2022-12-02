import requests
import datetime

HOST = 'http://127.0.0.1:5000'

# data = requests.post(f'{HOST}/user/', json={
#     'username': 'user',
#     'password': '12345678',
# })

data = requests.post(f'{HOST}/login/', json={
    'username': 'user',
    'password': '12345678'
})

print(data.json())
