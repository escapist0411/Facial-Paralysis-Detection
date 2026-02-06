import cv2
import os
import numpy as np
import mediapipe as mp

IMG_DIR = "data/segmentation/images"
MASK_DIR = "data/segmentation/masks"

os.makedirs(MASK_DIR, exist_ok=True)

files = os.listdir(IMG_DIR)
print(f"📂 Total images found: {len(files)}")

mp_face_mesh = mp.solutions.face_mesh

with mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True
) as face_mesh:

    for file in files:
        img_path = os.path.join(IMG_DIR, file)

        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"⏭️ Skipping non-image: {file}")
            continue

        img = cv2.imread(img_path)
        if img is None:
            print(f"❌ Cannot read image: {file}")
            continue

        h, w, _ = img.shape
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        result = face_mesh.process(rgb)
        mask = np.zeros((h, w), dtype=np.uint8)

        if result.multi_face_landmarks:
            points = [
                (int(lm.x * w), int(lm.y * h))
                for lm in result.multi_face_landmarks[0].landmark
            ]
            hull = cv2.convexHull(np.array(points))
            cv2.fillConvexPoly(mask, hull, 255)

        # SAME NAME, DIFFERENT EXTENSION
        base = os.path.splitext(file)[0]
        mask_path = os.path.join(MASK_DIR, base + ".png")

        cv2.imwrite(mask_path, mask)
        print(f"✅ Mask created: {base}.png")

print("🎉 All possible masks generated")
