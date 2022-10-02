import numpy as np
import cv2
import os
import face_recognition
import pyttsx3
import pyodbc
import datetime
from datetime import datetime as date
from getpass import getpass

path = 'C:\\Users\\User\\PycharmProject\\Mini_Project\\Photos'  # Setting the path for image folder
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')  # Reading each image and appending to imageslist
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])  # Taking out part of the image name to avoid extension
print(classNames)


def findEncodings(images):  # Method defined to encode images
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converting the images from defaultcolor(BGR) to RGB
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodeListKnown = findEncodings(images)
print('Encoded Successfully')  # Printing the length of images



def markoutAttendance(rollno, day, OutTime, OutDate):
    conn = pyodbc.connect(
        'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
    cursor = conn.cursor()
    sql = '''insert into attendance_db.dbo.mark_attendance2(rollno,current_day,OutTime,OutDate) values(?,?,?,?)'''
    val = (rollno, day, OutTime, OutDate)
    cursor.execute(sql, val)
    conn.commit()


cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Pixel size and scaling the image
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS, faceCurrentFrame)
    for encodeFace, faceLoc in zip(encodeCurrentFrame, faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)

        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)  # Finding the distance of the faces
        print(faceDistance)

        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            rollno = classNames[matchIndex].upper()
            print(rollno)

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, rollno, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            crctTime = datetime.datetime.now().time()
            crctDate = datetime.datetime.now().date()
            crctDay = date.today().strftime("%A")
            markoutAttendance(rollno, str(crctDay), str(crctTime), crctDate)

            '''if name != unMatch:
                markAttendance(name, str(crctTime), str(crctDate))
                name = unMatch'''

    cv2.imshow('Attendance Recording', img)
    cv2.waitKey(1)