import requests

# Python code to send a handshake request to the middleware
# Assuming the middleware is running on localhost:8000
url = 'http://localhost:8000/query'
data = {'query': 'SELECT * FROM your_table;'}
response = requests.post(url, json=data)
print(response.json())
