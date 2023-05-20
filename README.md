# beepy-2023
Este es un repositorio que contendrá todo lo abarcado en el taller "Python y Streamlit: El dúo dinámico para desplegar modelos de IA"

Para cada ejercicio existe una rama, tanto con instrucciones como con los archivos que se realicen en el taller!

## Ahora, crearemos una app de streamlit de prueba

## 1. Creación de un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Instalación de requisitos

```bash
pip install -r requirements.txt

```

## 3. Ejecución de streamlit.

Crea un nuevo archivo Python llamado `app.py` y agrega el siguiente código:

```python
import streamlit as st

st.title('Hola, Streamlit!')

st.write("Bienvenido a tu primera aplicación con Streamlit. ¡Disfrútalo!")
```

Podemos ver que se usa que usamos la libreria de streamlit (y específicamente, sus métodos) para poder añadir cosas. Por ejemplo, para los títulos llamamos a `st.title` y para texto normal, a `st.write`.

Añadamos una imagen de mi michi con `st.image`

```python
st.image('IMG_0009.JPG')
```

Podemos visualizar imágenes que subamos con `st.file_uploader`, como por ejemplo

```python
image = st.file_uploader(label="sube tu imagen")

if image:
    st.image(image)
```

Como esto, podemos hacer muchísimo más! Podemos revisar la documentación para revisar todas las posibilidades, (aquí)[https://docs.streamlit.io/]

Para levantar la aplicación, tenemos que ejecutar en consola

```bash
streamlit run app.py
```
