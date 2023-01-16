import numpy as np
import argparse
import cv2

# loading and converting the image into numpy array
image = cv2.imread("C:/Users/smart/Documents/Internship_Productize/TEST_IMAGES/3.jpg")

# convert image to greyscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(gray, (15,15), 0)

cv2.imshow("Gaussian blurr", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny Edge Detected", canny)

# finding the contours, counting and marking them
cnts, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("The number of coins in the image is : {}".format(len(cnts)))

#create a copy of the image
coins = image.copy()

# draw the contours in the actual color image copy
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Contours", coins)

cv2.waitKey(0)