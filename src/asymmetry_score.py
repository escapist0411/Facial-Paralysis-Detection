import numpy as np
def compute_asymmetry(landmarks):
    if landmarks is None: return 0
    left=np.mean([p[0] for p in landmarks[:200]])
    right=np.mean([p[0] for p in landmarks[200:400]])
    return round(abs(left-right)*100,2)
