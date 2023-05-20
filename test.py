import requests

url = 'http://localhost:8000/predict'
image_path = 'gatos.jpg'  # Ruta de la imagen que deseas enviar

with open(image_path, 'rb') as file:
    response = requests.post(url, files={'file': file})

print(response)
prediction = response.json()
print(prediction)
if 'cat' in prediction['prediction']:
    print(f"En la imagen hay un gato :D")
else:
    print("No hay un gato :(")