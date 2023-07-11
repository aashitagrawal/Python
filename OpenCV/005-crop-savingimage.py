import cv2
import numpy as np

def showImage(img):
    cv2.imshow("window",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



img = cv2.imread("sample.jpg")
showImage(img)
# Origin of an image is top-left
img_crop = img[0:300, 0:300]
showImage(img_crop)



#Saving an image
cv2.imwrite("sample_cropped.jpg",img_crop)