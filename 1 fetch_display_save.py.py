import cv2


# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread("blue_rose.jpg")
print(image.shape)
print(image)
print("width of the image in pixels is: {}".format(image.shape[1]))
print("height of the image in pixels is: {}".format(image.shape[0]))
print("channels present the image is: {}".format(image.shape[2]))

# load image into cv2 window
# wait for key press
# write image into another format
cv2.imshow("Image Title", image)
cv2.waitKey(0)
cv2.imwrite("rose.jpg", image)