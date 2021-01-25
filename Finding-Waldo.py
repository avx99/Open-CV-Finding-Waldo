import cv2
import numpy as np

image = cv2.imread("WaldoBeach.jpg")
cv2.imshow('Original',image)
cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
template = cv2.imread("Waldo.jpg")
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF) 
a,b,c,d=cv2.minMaxLoc(res)
o = d
r = (o[0]+50,o[1]+50)
cv2.rectangle(image,o,r,(0,0,255),5)
cv2.imshow('Waldo',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
