import cv2
import numpy as np

# Converting image to grayscale
img = cv2.imread("A:\CODING\Python\Libraries\Open CV\sample.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("window", img_gray)
cv2.waitKey(1500)

#Comparing shape
print("Shape of BGR image : ", img.shape)
print("Shape of GRAY image : ", img_gray.shape) # There is only one channel here