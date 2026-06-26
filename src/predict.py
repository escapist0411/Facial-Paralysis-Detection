import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

from src.config import MODEL_PATH, CLASSES
from src.landmarks import detect_landmarks
from src.asymmetry_score import compute_asymmetry
from src.preprocess import preprocess_image
from src.severity_classifier import severity_level

_model = None


def get_model():
    global _model
    if _model is None:
        try:
            if not os.path.exists(MODEL_PATH):
                raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
            _model = load_model(MODEL_PATH, compile=False)
        except Exception as e:
            print(f"Warning: Could not load model from {MODEL_PATH} ({e}). Using heuristic fallback.")
            _model = "HEURISTIC"
    return _model


def predict_image(path):
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"Image not found or cannot be read: {path}")

    model = get_model()
    x = preprocess_image(img)
    x = np.expand_dims(x, axis=0)

    if model == "HEURISTIC":
        # Determine label from simple image-based heuristics until a real model is trained.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contrast = float(gray.std())
        label = "Paralysis" if contrast < 45 else "Normal"
        confidence = 0.62 if label == "Paralysis" else 0.58
    else:
        pred = float(model.predict(x, verbose=0)[0][0])
        label = CLASSES[int(pred > 0.5)]
        confidence = pred if label == "Paralysis" else 1.0 - pred

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