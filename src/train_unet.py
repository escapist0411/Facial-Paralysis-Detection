import os
import cv2
import numpy as np
import tensorflow as tf
from src.unet_model import build_unet

IMG_SIZE = 128
DATA_DIR = "data/segmentation"
EPOCHS = 12
BATCH_SIZE = 4

def load_data():
    images, masks = [], []

    img_dir = os.path.join(DATA_DIR, "images")
    mask_dir = os.path.join(DATA_DIR, "masks")

    for file in os.listdir(img_dir):
        img_path = os.path.join(img_dir, file)
        mask_path = os.path.join(mask_dir, os.path.splitext(file)[0] + ".png")

        if not os.path.exists(mask_path):
            continue

        img = cv2.imread(img_path)
        mask = cv2.imread(mask_path, 0)

        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) / 255.0
        mask = cv2.resize(mask, (IMG_SIZE, IMG_SIZE))
        mask = (mask > 127).astype(np.float32)

        images.append(img)
        masks.append(mask)

    X = np.array(images)
    Y = np.expand_dims(np.array(masks), axis=-1)
    return X, Y

print("📥 Loading data...")
X, Y = load_data()
print("✅ Data loaded:", X.shape, Y.shape)

model = build_unet()
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X, Y,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_split=0.1
)

os.makedirs("models", exist_ok=True)
model.save("models/unet_face_segmentation.keras")
print("🎉 U-Net training complete and model saved")
