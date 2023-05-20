# Creando nuestra primera API

Estas instrucciones son para crear nuestra primera api 🔥

## 1. Creación de un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Instalación de requisitos

```bash
pip install fastapi uvicorn requests

```

## 3. Creación de tu primera API con FastAPI

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

```

En este código, estamos definiendo una nueva API con un único endpoint en la ruta `/`. Cuando alguien haga una petición GET a esta ruta, responderemos con un objeto JSON que dice `{"Hello": "World"}`.

## 4. Correr tu aplicación

Ahora puedes correr tu aplicación con el siguiente comando:

```
uvicorn main:app --reload

```

## 5. Acceder a tu API

### 5.1 Mediante navegador

Abre tu navegador web y ve a `http://localhost:8000`. Deberías ver tu mensaje de saludo: `{"Hello": "World"}`.

### 5.2 Mediante python

En python, escribiremos un script llamado `test.py` que contenga:

```python
import requests

response = requests.get("http://localhost:8000/")

print(response.json())
```

Ahora simplemente lo ejecutamos con

```bash
python test.py
```

## 6. Documentación interactiva

FastAPI genera automáticamente una documentación interactiva (swagger) para tu API. Puedes acceder a ella navegando a `http://localhost:8000/docs` en tu navegador web.