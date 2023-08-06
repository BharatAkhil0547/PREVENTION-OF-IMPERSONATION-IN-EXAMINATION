import os
import cv2 as cv
from cv2 import COLOR_BGR2RGB
from cv2 import COLOR_BGR2GRAY
from cv2 import imshow
import numpy as np
from collections import *
import datetime
import pandas as pd
from index_excel_loading import *
haar_cascade=cv.CascadeClassifier("C:\\Users\\chaitu\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
people=os.listdir("C:\\Users\\chaitu\\Desktop\\opencv\\group members")
face_recong=cv.face.LBPHFaceRecognizer_create()
face_recong.read("C:\\Users\\chaitu\\Desktop\\opencv\\recognizer1.yml")
capture=cv.VideoCapture(0)
c=[]
while True:
    res,frame=capture.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=haar_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        face_roi=gray[y:y+h,x:x+w]
        label,confidence=face_recong.predict(face_roi)
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if confidence>55:
            label="Unknown"
            c.append(label)
            cv.putText(frame,label,(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
            print(label,confidence)
        else:
            k=str(people[label])+"  "+str(confidence)
            cv.putText(frame,k,(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,0),thickness=2)
            c.append(str(people[label]))
            print(people[label],confidence)
        cv.imshow("frame",frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
a=datetime.datetime.now()
a=a.strftime("%X")
c=Counter(c)
s=''
m=max(list(c.values()))
for i in c:
    if c[i]==m:
        s=i
print(s)
cap=cv.VideoCapture(0)
while True:
    res,frame=cap.read()
    cv.putText(frame,s,(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,0),thickness=2)
    cv.imshow('final result',frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()

# Enrolling in excel file
df=pd.read_excel("C:\\Users\\chaitu\Desktop\\opencv\\abc.xlsx")
d={}
for (i,j) in enumerate(df['Student name']):
    d[j]=df.loc[i,'Register number']
print(d)

#excel-file loading
# if s!="Unknown":
#     excel_loading(s,d[s],a)


#date-wise excel files loading
if s!="Unknown":
    date_wise_loading(s,d[s],a)

