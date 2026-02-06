import mediapipe as mp, cv2
mp_face=mp.solutions.face_mesh
def detect_landmarks(image):
    mesh=mp_face.FaceMesh(static_image_mode=True)
    rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    res=mesh.process(rgb)
    if not res.multi_face_landmarks: return None
    pts=[]
    for lm in res.multi_face_landmarks[0].landmark:
        pts.append((lm.x,lm.y))
    return pts
