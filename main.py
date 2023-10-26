from model import model_pipeline
from typing import Union
from fastapi import FastAPI, UploadFile
from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    img = Image.open(image.file)

    result = model_pipeline(text, img)
    return {"answer": result}