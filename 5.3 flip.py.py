import imutils
import cv2

# loading and converting the image into numpy array
image = cv2.imread("dog.png")
cv2.imshow("Original", image)

flipped = cv2.flip(image, 0)
cv2.imshow("Vertical Flip", flipped)

flipped = cv2.flip(image, 1)
cv2.imshow("Horizontal Flip", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Both Flip", flipped)

cv2.waitKey(0)