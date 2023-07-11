import cv2
import numpy as np

def showImage(img):
    cv2.imshow("window",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = np.zeros((500,500,3))
showImage(img)

#Rectangle
cv2.rectangle(img, pt1=(100,100), pt2=(400,400), color=(255,255,0), thickness=-1) # Color is at BGR format, mixing Blue and Green will give teal color
showImage(img)
cv2.rectangle(img, pt1=(100,100), pt2=(400,400), color=(0,255,255), thickness=3) # Mixing green and red gives yellow colour.
showImage(img)

#Circle
cv2.circle(img, center=(250,250), radius=150, color=(255,0,255), thickness=3) # Mixing blue and red colour gives pink colour.
showImage(img)
cv2.circle(img, center=(250,250), radius=212, color=(255,0,0), thickness=3) # Blue colour.
showImage(img)

#Line
cv2.line(img, pt1=(50,50), pt2=(450,450), color=(0,0,255), thickness=3)
showImage(img)
cv2.line(img, pt1=(500,0), pt2=(0,500), color=(0,0,255), thickness=3)
showImage(img)

#Text
cv2.putText(img, text="Hare Krishna", org=(0,500), fontScale=1, color=(255,255,255), thickness=1, fontFace=cv2.QT_FONT_NORMAL, lineType=cv2.LINE_4)
showImage(img)
cv2.putText(img, text="Hare Krishna", org=(100,100), fontScale=1, color=(255,255,255), thickness=1, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, lineType=cv2.LINE_4)
showImage(img)