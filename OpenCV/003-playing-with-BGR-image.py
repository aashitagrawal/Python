import cv2
import numpy as np

def showImage(img):
    cv2.imshow("window", img)
    cv2.waitKey(0)

img = cv2.imread("rainbow.jpg")
showImage(img)

img_blue = img.copy()
img_blue[:,:,0]=0 # Making intensity of blue channel zero, Mixing green and red colour gives yellow colour.
showImage(img_blue)

img_green = img.copy()
img_green[:,:,1]=0 # Making intensity of green channel zero, Mixing blue and red colour gives purple colour.
showImage(img_green)

img_red = img.copy()
img_red[:,:,2]=0 # Making intensity of red channel zero, Mixing green and blue colour gives teal colour.
showImage(img_red)

# Showing all side by side
newimg = np.hstack((img_blue, img_green, img_red))
showImage(newimg)



imgOnlyBlue = img.copy()
imgOnlyBlue = imgOnlyBlue[:,:,0]

imgOnlyGreen = img.copy()
imgOnlyGreen = imgOnlyGreen[:,:,0]

imgOnlyRed = img.copy()
imgOnlyRed = imgOnlyRed[:,:,0]

newimg = np.hstack((imgOnlyBlue, imgOnlyGreen, imgOnlyRed))
showImage(newimg)