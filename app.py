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