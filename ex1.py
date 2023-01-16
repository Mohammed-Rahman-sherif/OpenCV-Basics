import cv2
import numpy as np 

img = cv2.imread("dog.png")

print(img.shape)
cv2.imshow("The Dog",img)
cv2.waitKey(0)

(b,g,r)=img[0,0]

print("pixel value R={} G={} B={}".format(r,g,b))

img[0,0]=(255,0,0)
(b,g,r)=img[0,0]
print("pixel value R={} G={} B={}".format(r,g,b))

cv2.imshow("my image",img)
cv2.waitKey(0)

img[0:100,0:100]=(0,255,0)
cv2.imshow("image",img)
cv2.waitKey(0)