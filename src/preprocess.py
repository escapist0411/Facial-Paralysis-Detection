import cv2, os, numpy as np
from src.config import IMG_SIZE
def load_dataset(dataset_path):
    X,y=[],[]
    for label,folder in enumerate(["normal","paralysis"]):
        path=os.path.join(dataset_path,folder)
        for f in os.listdir(path):
            img=cv2.imread(os.path.join(path,f))
            img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))/255.0
            X.append(img); y.append(label)
    return np.array(X), np.array(y)
