import imutils
import cv2

# loading and converting the image into numpy array
image = cv2.imread("dog.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# crop the image
# start y 15: end y 222 , start x 150: endx 400
cropped = image[15:222, 150:400]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
