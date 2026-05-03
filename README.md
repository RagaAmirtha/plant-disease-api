# 🌿 PlantGuard-API

AI-powered Plant Disease Detection and Explanation System using Deep Learning + LLM integration.

---

## 📌 Overview

**PlantGuard-API** is a FastAPI-based application that detects plant diseases from images using a trained deep learning model and provides detailed explanations using a Large Language Model (LLM).

This project supports **sustainable agriculture (SDG Goal 2: Zero Hunger 🌍)** by helping farmers and researchers quickly identify plant diseases and take corrective action.

---

## 🚀 Features

* 🌱 Upload plant leaf images for disease detection
* 🤖 Deep Learning model (Keras) for classification
* 🧠 LLM integration (LLaMA3 via Ollama) for explanations
* ⚡ FastAPI backend with interactive Swagger UI
* 🐳 Docker support for easy deployment
* 📊 Returns:

  * Disease name
  * Confidence score
  * Cause, symptoms, cure, and prevention

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **ML Model:** TensorFlow / Keras
* **Image Processing:** Pillow, NumPy
* **LLM:** Ollama (LLaMA3)
* **Deployment:** Docker

---

## 📂 Project Structure

```
plant-disease-api/
│── main.py              # FastAPI application
│── keras_model1.h5      # Trained ML model
│── labels.txt           # Class labels
│── requirements.txt     # Dependencies
│── Dockerfile           # Container setup
│── README.md            # Project documentation
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the repository

```
git clone https://github.com/RagaAmirtha/plant-disease-api
cd plant-disease-api
```

### 2️⃣ Create virtual environment (optional)

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the API

```
uvicorn main:app --reload
```

### 5️⃣ Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Setup

### Build image

```
docker build -t plant-disease-api .
```

### Run container

```
docker run -p 8000:8000 plant-disease-api
```

---

## 🧠 LLM Integration (Ollama)

Make sure Ollama is running:

```
ollama run llama3
```

The API calls:

```
http://localhost:11434/api/generate
```

---

## 📡 API Endpoint

### 🔹 POST `/predict/`

Upload an image file to get prediction.

#### Request:

* Form-data → `file` (image)

#### Response:

```json
{
  "class_name": "Early Blight",
  "confidence_score": 0.95,
  "llm_explanation": "Detailed explanation..."
}
```

---

## 🧪 Example Workflow

1. Upload plant leaf image
2. Model predicts disease
3. LLM explains:

   * Cause
   * Symptoms
   * Cure
   * Prevention

---

## 🎯 Use Cases

* Smart agriculture systems
* Farmer assistance tools
* Research and plant pathology studies
* AI-based crop monitoring

---

## 🌍 SDG Alignment

This project supports:

**Goal 2: Zero Hunger**

* Improves crop health monitoring
* Reduces agricultural loss
* Promotes sustainable farming

---

## 📸 Demo

Use Swagger UI:

```
/docs
```

Upload an image and test the API directly.

---

## ⚠️ Notes

* GPU is optional (runs on CPU)
* LLM requires Ollama running locally
* Model accuracy depends on training dataset

---

## 👩‍💻 Author

**Raga Amirtha.A**
**RA2311026050054**
GitHub: https://github.com/RagaAmirtha

---

## 📄 License

This project is for academic and educational purposes.

---

## ⭐ Acknowledgment

* TensorFlow & Keras
* FastAPI
* Ollama LLM

---

## 🔥 Future Improvements

* Add frontend UI
* Deploy to cloud (AWS / GCP)
* Improve model accuracy
* Multi-crop disease detection

---
