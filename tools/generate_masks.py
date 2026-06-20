import os
import cv2
import numpy as np
import mediapipe as mp
import glob
from tqdm import tqdm

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)

def generate_dataset():
    input_dirs = ["dataset/normal", "dataset/paralysis"]
    out_img_dir = "data/segmentation/images"
    out_mask_dir = "data/segmentation/masks"

    os.makedirs(out_img_dir, exist_ok=True)
    os.makedirs(out_mask_dir, exist_ok=True)

    image_paths = []
    for d in input_dirs:
        image_paths.extend(glob.glob(f"{d}/*.*"))

    print(f"Found {len(image_paths)} images. Generating masks...")

    success_count = 0
    for idx, path in enumerate(tqdm(image_paths)):
        img = cv2.imread(path)
        if img is None:
            continue

        h, w, _ = img.shape
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_img)

        if not results.multi_face_landmarks:
            continue

        # Extract landmarks and create a convex hull for the face mask
        landmarks = results.multi_face_landmarks[0].landmark
        pts = np.array([(int(lm.x * w), int(lm.y * h)) for lm in landmarks], dtype=np.int32)
        hull = cv2.convexHull(pts)

        # Draw the mask
        mask = np.zeros((h, w), dtype=np.uint8)
        cv2.fillConvexPoly(mask, hull, 255)

        # Save to the dataset folder
        base_name = f"face_{idx:04d}"
        cv2.imwrite(os.path.join(out_img_dir, f"{base_name}.png"), img)
        cv2.imwrite(os.path.join(out_mask_dir, f"{base_name}.png"), mask)
        success_count += 1

    print(f"Successfully generated {success_count} masks.")

if __name__ == "__main__":
    generate_dataset()
