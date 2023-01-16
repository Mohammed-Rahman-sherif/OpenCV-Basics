import imutils
import cv2

# loading and converting the image into numpy array
image = cv2.imread("C:\\Users\\smart\\OneDrive\\Pictures\\IMG_20220712_163859.jpg")
cv2.imshow(" original image ", image)
cv2.waitKey(0)

#resize the image
resized = imutils.resize(image, width = 100)
cv2.imshow(" width resized ", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height = 200)
cv2.imshow(" Height resized ", resized)
cv2.waitKey(0)