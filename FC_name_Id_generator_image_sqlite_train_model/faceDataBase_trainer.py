import os
import cv2
import numpy as np
from PIL import Image

#creating a recognizer

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'

def getImagesWithID(path):
    imagePaths=[os.path.join(path, f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        #ID=int(os.path.split(imagePath)[-1].split('.')[0])
        ID = int(imagePath.split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow('training', faceNp)
        cv2.waitKey(1)
    return np.array(IDs), faces

Ids, faces = getImagesWithID(path)
recognizer.train(faces, Ids)

if not os.path.exists('models'):
    os.makedirs('models')

recognizer.save('models/trained_from_sqliteDB.yml')
cv2.destroyAllWindows()
