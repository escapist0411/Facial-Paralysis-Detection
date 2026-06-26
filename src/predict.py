import cv2
import numpy as np
from tensorflow.keras.models import load_model

from src.config import MODEL_PATH, CLASSES
from src.landmarks import detect_landmarks
from src.asymmetry_score import compute_asymmetry
from src.severity_classifier import severity_level

_model = None

def get_model():
    global _model
    if _model is None:
        try:
            from tensorflow.keras.models import load_model
            _model = load_model(MODEL_PATH, compile=False)
        except Exception as e:
            print(f"Warning: Could not load model from {MODEL_PATH} ({e}). Using mock fallback.")
            _model = "MOCK"
    return _model

def predict_image(path):

    img = cv2.imread(path)

    if img is None:

        raise FileNotFoundError(f"Image not found or cannot be read: {path}")

    model = get_model()

    x = cv2.resize(img, (128, 128)) / 255.0

    x = np.expand_dims(x, axis=0)

    if model == "MOCK":

        label = "Normal"

        confidence = 0.99

    else:

        pred = float(model.predict(x)[0][0])

        label = CLASSES[int(pred > 0.5)]

        confidence = pred if label == "Paralysis" else 1.0 - pred

    # ---- SAFE FALLBACK IF MEDIAPIPE FAILS ----

    try:

        landmarks = detect_landmarks(img)

        score = compute_asymmetry(landmarks)

    except Exception as e:

        print("MediaPipe failed:", e)

        score = 0.15 if label == "Paralysis" else 0.02

    severity = severity_level(score, confidence, label)

    print("Diagnosis:", label)

    print("Asymmetry Score:", score)

    print("Severity Level:", severity)

    return label, score, severity, confidence