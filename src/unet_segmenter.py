import cv2
import numpy as np
import tensorflow as tf

MODEL_PATH = "models/unet_face_segmentation.keras"

_model = None

def get_model():
    global _model
    if _model is None:
        try:
            _model = tf.keras.models.load_model(MODEL_PATH, compile=False)
        except Exception as e:
            print(f"Warning: Could not load U-Net model from {MODEL_PATH} ({e}). Using mock fallback.")
            _model = "MOCK"
    return _model

def post_process_mask(mask):
    """
    Improves segmentation mask quality
    """

    kernel = np.ones((5, 5), np.uint8)

    # Remove small noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Fill small holes
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Smooth edges
    mask = cv2.GaussianBlur(mask.astype(np.float32), (7, 7), 0)

    # Re-binarize
    mask = (mask > 0.5).astype(np.uint8)

    return mask


def run_unet_segmentation(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found")

    model = get_model()
    h, w, _ = image.shape

    img = cv2.resize(image, (128, 128))
    img = img / 255.0

    if model == "MOCK":
        # Create a dummy circle mask in the center
        mask = np.zeros((128, 128), dtype=np.uint8)
        cv2.circle(mask, (64, 64), 40, 1, -1)
    else:
        pred = model.predict(img[None, ...], verbose=0)[0, :, :, 0]
        mask = (pred > 0.5).astype(np.uint8)

    # ⬇️ NEW: Post-processing
    mask = post_process_mask(mask)

    # Resize back to original size
    mask = cv2.resize(mask, (w, h), interpolation=cv2.INTER_NEAREST)

    return mask
