import numpy as np
import cv2

# loading and converting the image into numpy array
image = cv2.imread("dog.png")
#cv2.imshow("Original", image)
#cv2.waitKey(0)

#split the image based on channels
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

#merge back the channels
merged = cv2.merge([B, G, R])
cv2.imshow("merged", merged)
cv2.waitKey(0)