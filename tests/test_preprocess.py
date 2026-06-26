import numpy as np

from src.preprocess import preprocess_image


def test_preprocess_image_normalizes_and_resizes():
    image = np.zeros((240, 320, 3), dtype=np.uint8)

    processed = preprocess_image(image, target_size=(128, 128))

    assert processed.shape == (128, 128, 3)
    assert processed.dtype == np.float32
    assert processed.min() >= 0.0
    assert processed.max() <= 1.0
