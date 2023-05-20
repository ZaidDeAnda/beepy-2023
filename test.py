import requests

nombre = input("¿Como te llamas? ")
response = requests.get(f"http://localhost:8000/hola/{nombre}")

print(response.json())