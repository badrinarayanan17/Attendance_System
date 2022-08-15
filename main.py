
import numpy as np
import cv2
import os
import face_recognition
import pyttsx3
import pyodbc
import datetime
from datetime import datetime as date
from getpass import getpass




path = 'C:\\Users\\User\\PycharmProject\\Mini_Project\\Photos' #Setting the path for image folder
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)


for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}') #Reading each image and appending to imageslist
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0]) #Taking out part of the image name to avoid extension
print(classNames)

def findEncodings(images): #Method defined to encode images
    encodelist = []
    for img in images:
     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Converting the images from defaultcolor(BGR) to RGB
     encode = face_recognition.face_encodings(img)[0]
     encodelist.append(encode)
    return encodelist

encodeListKnown = findEncodings(images)
print('Encoded Successfully') #Printing the length of images

def markAttendance(rollno,day,InTime,InDate):
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
    cursor = conn.cursor()
    sql = '''insert into attendance_db.dbo.mark_attendance(rollno,current_day,InTime,InDate) values(?,?,?,?)'''
    val = (rollno,day,InTime,InDate)
    cursor.execute(sql,val)
    conn.commit()
    
cap = cv2.VideoCapture(1)


while True:
    success,img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25) #Pixel size and scaling the image
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS,faceCurrentFrame)
    for encodeFace,faceLoc in zip(encodeCurrentFrame,faceCurrentFrame):
     matches = face_recognition.compare_faces(encodeListKnown,encodeFace)

     faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace) #Finding the distance of the faces
     print(faceDistance)

     matchIndex =np.argmin(faceDistance)


     if matches[matchIndex]:
        rollno = classNames[matchIndex].upper()
        print(rollno)

        y1,x2,y2,x1 = faceLoc
        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        cv2.putText(img,rollno,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        crctTime = datetime.datetime.now().time()
        crctDate = datetime.datetime.now().date()
        crctDay = date.today().strftime("%A")
        markAttendance(rollno,str(crctDay),str(crctTime),crctDate)
        '''if name != unMatch:
            markAttendance(name, str(crctTime), str(crctDate))
            name = unMatch'''

    cv2.imshow('Attendance Recording', img)
    cv2.waitKey(1)


'''
imgvirat = face_recognition.load_image_file('Photos/Virat.jpg')
imgvirat = cv2.cvtColor(imgvirat,cv2.COLOR_RGB2BGR)
imgtest = face_recognition.load_image_file('Photos/Virat Test.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_RGB2BGR)

faceLoc = face_recognition.face_locations(imgvirat)[0]
encodeVirat = face_recognition.face_encodings(imgvirat)[0]
cv2.rectangle(imgvirat,(faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255),2)
print(faceLoc)

faceLocTest = face_recognition.face_locations(imgtest)[0]
encodeViratTest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceLocTest[3],faceLocTest[0],faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeVirat],encodeViratTest)
faceDis = face_recognition.face_distance([encodeVirat],encodeViratTest)
print(results,faceDis)
cv2.putText(imgtest,f'{results}{faceDis[0]}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


cv2.imshow('Virat',imgvirat)
cv2.imshow('Virat Test',imgtest)
cv2.waitKey(0)
'''


