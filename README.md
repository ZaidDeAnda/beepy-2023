# Creando nuestra primera API

Estas instrucciones son para crear nuestra primera api 🔥

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