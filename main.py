import requests
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Plant Disease Analysis API")

# Load model and labels
MODEL_PATH = "keras_model1.h5"
LABELS_PATH = "labels.txt"

model = load_model(MODEL_PATH, compile=False)
class_names = open(LABELS_PATH, "r").readlines()


# ✅ LLM FUNCTION
def get_llm_explanation(disease):
    prompt = f"""
    Plant disease: {disease}

    Explain clearly:
    - Cause
    - Symptoms
    - Cure
    - Prevention
    """

    try:
        response = requests.post(
            "http://host.docker.internal:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]

    except Exception as e:
        return f"LLM error: {str(e)}"


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=308)


@app.post("/predict/")
def predict_image(file: UploadFile = File(...)):
    try:
        # Image preprocessing
        image = Image.open(file.file).convert("RGB")
        image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

        image_array = np.asarray(image)
        normalized = (image_array.astype(np.float32) / 127.5) - 1

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized

        # Prediction
        prediction = model.predict(data)
        index = np.argmax(prediction)

        class_name = class_names[index].strip()
        confidence_score = float(prediction[0][index])

        print("Prediction:", class_name)
        print("Calling LLM...")

        # ✅ LLM CALL (SAFE)
        llm_output = get_llm_explanation(class_name)

        # Response
        return JSONResponse(
            content={
                "class_name": class_name,
                "confidence_score": confidence_score,
                "llm_explanation": llm_output
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))