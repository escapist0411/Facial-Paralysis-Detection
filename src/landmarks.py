import cv2

try:
    import mediapipe as mp
    mp_face = mp.solutions.face_mesh
    MEDIAPIPE_OK = True
except Exception as e:
    print("MediaPipe import failed:", e)
    MEDIAPIPE_OK = False


def detect_landmarks(image):
    if not MEDIAPIPE_OK:
        return None

    try:
        with mp_face.FaceMesh(static_image_mode=True) as mesh:
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            res = mesh.process(rgb)

            if not res.multi_face_landmarks:
                return None

            pts = []
            for lm in res.multi_face_landmarks[0].landmark:
                pts.append((lm.x, lm.y))
            return pts

    except Exception as e:
        print("Landmark detection failed:", e)
        return None