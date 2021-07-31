import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'setData'

def getImagesID(path):
    imagePath = [os.path.join(path,f) for f in os.listdir(path)]

    print(imagePath)

    faces = []
    IDs = []

    for imagePath in imagePath:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg,'uint8')
        print(faceNp)
        ID = int(imagePath.split('\\')[1].split('.')[1])

        faces.append(faceNp)
        IDs.append(ID)

        cv2.imshow('training', faceNp)
        cv2.waitKey(5000)

        return faces, IDs

faces,IDs = getImagesID(path)

recognizer.train(faces,np.array(IDs))

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')

recognizer.save('recognizer/trainingData.yml')

cv2.destroyAllWindows()