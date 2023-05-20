import requests

response = requests.get("http://localhost:8000/")

print(response.json())