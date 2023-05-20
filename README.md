# Creando una API para desplegar YOLO

Ahora levantaremos una API que regrese una respuesta del modelo yolo al recibir una imagen.

## 1. Creación de un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Instalación de requisitos

```bash
pip install -r requirements.txt

```

## 3. Ejecución de yolo

Primero, importamos la librería de ultralytics

```python
from ultralytics import YOLO
```

Luego, cargamos el modelo

```python
model = YOLO('yolov8n.pt')
```

Y ejecutamos inferencia en una imagen de panque

```python
results = model("IMG_0009.JPG", save=True)
```

El argumento `save` es para poder guardar la imagen con la caja de predicción, que encontrarán en el folder `runs/predictx/IMG_0009.JPG` (o en lugar de IMG_'0009.JPG', la imagen que decidan usar)

Imprimimos el resultado para poder debuggearlo

```python
print(results)
```

Observamos que es una lista, accedemos a su único elemento

```python
print(results[0])
```

Vemos que tiene un atributo `boxes`, accedemos a el 
Ojo, también tiene un atributo `names`, del que podemos obtener el nombre de la clase

```python
print(results[0].boxes)
```

Dentro de este resultado, hay un parámetro `cls`, que nos indica las clases de las predicciones, imprimámoslo

```python
print(results[0].boxes.cls)
```

Ahora revisemos a que corresponde esa clase en `results[0].names`

```python
print(results[0].names[15])
```

Tenemos un michi detectado!

## 4. Despliegue de yolo en una API

Realicemos una API que te diga si una imagen contiene un michi o no.

Empezamos por la api:

```python
from fastapi import FastAPI, File, UploadFile, Form
from ultralytics import YOLO
from PIL import Image
import io

model = YOLO('yolov8n.pt')
names = model.names

app = FastAPI()

print("api ejecutándose")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content)).convert("RGB")
    results = model.predict(source=image)
    results = [names[int(result)] for result in results[0].boxes.cls]
    return {"prediction": results}
```

Recibimos en la ruta `/predict` una imagen. Ojo, no se puede recibir una imagen en la ruta (en realidad, puedes usar base 64 para pasarla, pero es un poco mas complicado). Por lo que fastAPI nos permite activar la opción para recibir archivos. Después, lo leemos, convertimos la información de Bytes a una imagen RGB, y realizamos la predicción con el modelo. Ahora solo regresamos las clases que predijo (con un poquito de comprension de listas para regresar los nombres en lugar de los numeros de las clases, mas info (aqui)[https://www.w3schools.com/python/python_lists_comprehension.asp])

Ahora, como este recibe un archivo, solo podemos testearlos con scripts (o aplicaciones como postman). Por ello, realizamos un script `test.py` que contenga:

```python
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
```

Donde solo cargamos una imagen en memoria, armamos un request con ella y la mandamos. De ahí, checamos si en la respuesta en la llave de predicción existe la clase "gato", y de ser así, imprime que hay un gato!