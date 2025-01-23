import requests

url = "http://localhost:8001/health"


response = requests.get(url)

print(response.json())
print(response.status_code)