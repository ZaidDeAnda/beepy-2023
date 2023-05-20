# Creacion de API parametrizada

Ahora crearemos una API a la que le podamos pasar un parámetro

## 1. Preparar entorno

Si seguiste la creación de la primer api, puedes usar el mismo entorno. Para activarlo, solo tienes que escribir

```bash
source venv/bin/activate
```

Si no, puedes instalarlo usando

```bash
pip install -r requirements.txt
```

## 2. Creación de la API

```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/hola/{nombre}")
def read_root(nombre: str):
    return {"Hola!": nombre}

```

## 3. Correr tu aplicación

Ahora puedes correr tu aplicación con el siguiente comando:

```
uvicorn main:app --reload

```

## 4. Acceder a tu API

### 4.1 Mediante navegador

Abre tu navegador web y ve a `http://localhost:8000/hola/Panque`. Deberías ver tu mensaje de saludo: `{"Hola!": "Panque"}`.

### 4.2 Mediante python

En python, escribiremos un script llamado `test.py` que contendrá:

```python
import requests

nombre = input("¿Como te llamas? ")
response = requests.get(f"http://localhost:8000/{nombre}")

print(response.json())
```

Ahora simplemente lo ejecutamos con 

```
python test.py
```