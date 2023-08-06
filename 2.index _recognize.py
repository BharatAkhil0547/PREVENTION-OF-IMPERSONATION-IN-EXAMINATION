from distutils.util import change_root
import os
import cv2 as cv
import numpy as np
from collections import Counter
main_path="C:\\Users\\chaitu\\Desktop\\opencv\\group members\\"
#main_path="C:\\Users\\chaitu\\Desktop\\opencv\\people"
#"C:\Users\chaitu\Desktop\opencv\group members\\"
res=os.listdir("C:\\Users\\chaitu\\Desktop\\opencv\\group members")
print(res)
face_casacde=cv.CascadeClassifier("C:\\Users\\chaitu\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
people=os.listdir("C:\\Users\\chaitu\\Desktop\\opencv\\group members")
#people=['markzukerberg','stevejobs','sundarpichai']
features=[]
label=[]
def training():
    for i in people:
        res=os.path.join(main_path,i)
        labels=people.index(i)
        for j in os.listdir(res):
            img_path=os.path.join(res,j)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces=face_casacde.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in faces:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                label.append(labels)
training()
print("*****training done******")
# print(features,len(features))
print(label,len(label))
features=np.array(features,dtype="object")
label=np.array(label)
face_recong=cv.face.LBPHFaceRecognizer_create()
face_recong.train(features,label)
change="C:\\Users\\chaitu\\Desktop\\opencv"
os.chdir(change)
face_recong.save('recognizer1.yml')
