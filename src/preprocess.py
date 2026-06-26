import os
import cv2
import numpy as np
from src.config import IMG_SIZE


def preprocess_image(image, target_size=(IMG_SIZE, IMG_SIZE)):
    if image is None:
        raise ValueError("Image is empty")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    image = image.astype(np.float32) / 255.0
    return image


def load_dataset(dataset_path):
    X, y = [], []
    for label, folder in enumerate(["normal", "paralysis"]):
        path = os.path.join(dataset_path, folder)
        for f in os.listdir(path):
            img_path = os.path.join(path, f)
            img = cv2.imread(img_path)
            if img is None:
                continue
            X.append(preprocess_image(img))
            y.append(label)
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.int32)
