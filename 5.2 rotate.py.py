
import imutils
import cv2


# loading and converting the image into numpy array
image = cv2.imread("dog.png")

# rotate the image
rotated = imutils.rotate(image, 180)
cv2.imshow("180 rotated", rotated)
cv2.waitKey(0)