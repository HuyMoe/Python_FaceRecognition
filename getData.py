import cv2
import numpy
import sqlite3
import os

def insertUpdate(id, name, age, sex):

    conn = sqlite3.connect("D:/python/Face_Recognition/Data.db")

    query = "SELECT * FROM people WHERE ID= " + str(id)

    cursor = conn.execute(query)

    isRecordExist = 0

    for row in cursor:

        isRecordExist = 1

    if(isRecordExist == 0):
        query = "INSERT INTO people(ID, Name, Age, Sex) values("+str(id)+",'"+str(name)+"','"+str(age)+"','"+str(sex)+"')"
    else:
        query = "UPDATE people SET Name = '"+str(name)+"', Age= '"+str(age)+"', Sex= '"+str(sex)+"' Where ID= " + str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

id = input('Enter your ID: ')
name = input('Enter your Name: ')
age = input('Enter your Age: ')
sex = input('Enter your Sex: ')
insertUpdate(id, name, age, sex)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
sampleNum = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if not os.path.exists('setData'):
        os.makedirs('setData')
    sampleNum += 1

    cv2.imwrite('setData/User.'+str(id)+'.'+str(sampleNum)+'.jpg', gray[y:y+h,x:x+w])

    cv2.imshow('face', frame)
    cv2.waitKey(1)

    if sampleNum > 200:
        break


cap.release()
cv2.destroyAllWindows()