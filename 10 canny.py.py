import numpy as np
import argparse
import cv2

# loading and converting the image into numpy array
image = cv2.imread("C:/Users/smart/Documents/Internship-2/dirty_plate_5.jpg")

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Gaussian blurr", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny Edge Detected", canny)
cv2.waitKey(0)