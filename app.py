from fastapi import FastAPI

app = FastAPI()

@app.get("/hola/{nombre}")
def read_root(nombre: str):
    return {"Hola!": nombre}
