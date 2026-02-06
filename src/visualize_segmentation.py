import cv2
import numpy as np

def create_segmentation_overlay(image_path, mask_path, output_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (512, 512))

    mask = cv2.imread(mask_path, 0)
    mask = cv2.resize(mask, (512, 512))

    # Create colored mask
    colored_mask = np.zeros_like(img)
    colored_mask[mask > 0] = (0, 255, 0)  # green

    # Overlay
    overlay = cv2.addWeighted(img, 0.75, colored_mask, 0.25, 0)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(overlay, contours, -1, (0, 0, 255), 2)

    # Fake landmarks (for demo / viva)
    h, w = mask.shape
    for (x, y) in [(w//3, h//2), (2*w//3, h//2), (w//2, h//3)]:
        cv2.circle(overlay, (x, y), 4, (255, 0, 0), -1)

    cv2.imwrite(output_path, overlay)
