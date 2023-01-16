import numpy as np
import cv2

# loading and converting the image into numpy array
image = cv2.imread("C:/Users/smart/Documents/Internship-2/printed_plate_2.jpg")

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale", image)
cv2.waitKey(0)

# implement gaussian blurr
blurred = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Gaussian blurr", blurred)
cv2.waitKey(0)
#simple Thresholding using binary
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)
#simple Thresholding using inv binary
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Inv Binary", threshInv)
cv2.waitKey(0)
cv2.imshow("Only Coins", cv2.bitwise_and(image, image, mask = threshInv))
cv2.waitKey(0)

#adaptive thresholding using mean
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive mean", thresh)
cv2.waitKey(0)
#adaptive thresholding using gaussian
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive gaussian", thresh)

cv2.waitKey(0)