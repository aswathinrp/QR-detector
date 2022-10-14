import numpy as np
import cv2
from pyzbar.pyzbar import decode

img= cv2.imread('1.jpg')
code = decode(img)
print(code)

for barcode in decode(img):
    print(barcode.data)
    mydata = barcode.data.decode('utf-8')
    print(mydata)
    # pts = np.array([barcode.polygon],np.int32)
    # pts = pts.reshape((-1,1,2))
    # cv2.polylines(img,[pts],True,(255,0,255),5)
    # pts2 = barcode.rect
    cv2.putText(img,mydata,(20,20),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),3)
cv2.imshow('result',img)
cv2.waitKey(10)


