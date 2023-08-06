import cv2 as cv
import numpy as np
import pandas as pd
import os
import time
res=os.getcwd()
print(os.listdir(res))
Name=input("Enter the name : ")
Regd_number=int(input("Enter the resgister number : "))
df=pd.read_excel("C:\\Users\\chaitu\Desktop\\opencv\\abc.xlsx")
x=list(df['Register number'])
if Regd_number not in x:
    df.loc[len(df.index)]=[Name,Regd_number]
    df.to_excel("C:\\Users\\chaitu\Desktop\\opencv\\abc.xlsx",index=False)
    create_folder=os.path.join(res,Name)
    os.mkdir(create_folder)
    os.chdir(create_folder)
    cap=cv.VideoCapture(0)
    time.sleep(1.5)
    count=0
    while True:
        print("image loading",count)
        res,frame=cap.read()
        cv.imshow("loading",frame)
        cv.imwrite("frame%d.jpg" % count,frame)
        if cv.waitKey(50) & 0xFF==ord('a'):
            break
        if count==50:
            break
        count=count+1
    cap.release()
    cv.destroyAllWindows() 
else:
    print("those details are already filled in excel file")

