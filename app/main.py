from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import io, json, numpy as np, tensorflow as tf

app = FastAPI(title="Sports Image Classifier")
model = tf.keras.models.load_model("models/model.h5")
labels = json.load(open("models/labels.json"))
IMG_SIZE = (128, 128)

def preprocess(img: Image.Image):
    img = img.convert("RGB").resize(IMG_SIZE)
    arr = np.asarray(img, dtype=np.float32) / 255.0
    return arr[None, ...]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in {"image/jpeg", "image/png"}:
        raise HTTPException(415, "KUN JPG/PNG")
    img = Image.open(io.BytesIO(await file.read()))
    x = preprocess(img)
    probs = model.predict(x, verbose=0)[0]
    i = int(np.argmax(probs))
    return {"label": labels[i], "prob": float(probs[i])}
