import cv2
import numpy as np
from tensorflow.keras.models import load_model

from src.config import MODEL_PATH, CLASSES
from src.landmarks import detect_landmarks
from src.asymmetry_score import compute_asymmetry
from src.severity_classifier import severity_level

model = load_model(MODEL_PATH, compile=False)




def predict_image(path):
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"Image not found or cannot be read: {path}")


    x = cv2.resize(img, (128, 128)) / 255.0
    x = np.expand_dims(x, axis=0)

    pred = model.predict(x)[0][0]
    label = CLASSES[int(pred > 0.5)]

    landmarks = detect_landmarks(img)
    score = compute_asymmetry(landmarks)

    severity = severity_level(score)

    print("Diagnosis:", label)
    print("Asymmetry Score:", score)
    print("Severity Level:", severity)

    return label, score, severity
