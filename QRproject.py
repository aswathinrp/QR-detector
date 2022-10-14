import numpy as np
import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()
print(myDataList)

while True:
    success,img = cap.read()
    
    for barcode in decode(img):
        print(barcode.data)
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        if mydata in myDataList:
           myoutput = 'Authorised'
        else:
            myoutput = 'Un-Authorised'
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myoutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),3)
    cv2.imshow('result',img)
    cv2.waitKey(1)

