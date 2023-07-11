import cv2
import numpy as np

# Read and Displaying an Image
img = cv2.imread("A:\CODING\Python\Libraries\Open CV\sample.jpg")
print("Type of cv2 images : ",type(img)) #numpy array
print("Shape of this image : ",img.shape)

cv2.imshow("window", img)
cv2.waitKey(0) #The window will not close
# cv2.waitKey(1000) #The window will close in 1000 milliseconds
