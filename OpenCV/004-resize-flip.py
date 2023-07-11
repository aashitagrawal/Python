import cv2
import numpy as np

def showImage(img):
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("sample.jpg")
print("Current shape:", img.shape)
showImage(img)

img_resize = cv2.resize(img, (700, 800)) # (width, height)
print("Resized:", img_resize.shape) # (height, width, channels)
showImage(img_resize)

img_resize = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) # (width, height)
print("Resized:", img_resize.shape) # (height, width, channels)
showImage(img_resize)


# Flipping
img_flip = cv2.flip(img_resize, 0)
img_flip1 = cv2.flip(img_resize, 1)
img_flip2 = cv2.flip(img_resize, -1)
new_image = np.hstack((img_resize, img_flip, img_flip1, img_flip2))
showImage(new_image)