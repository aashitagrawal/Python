import cv2
import numpy as np

flag = False
a = -1
b = -1
p = -1
q = -1

def crop(event, x, y, flags, params):
    global flag,a,b,p,q
    if event==cv2.EVENT_LBUTTONDOWN:
        flag = True
        a = x
        b = y
    elif event==cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, pt1=(a,b), pt2=(x,y), color=(0,255,255), thickness=1)
        flag = False
        p = x
        q = y

cv2.namedWindow("window")
cv2.setMouseCallback("window",crop)


img = cv2.imread("plane.jpg")
img_copy = img.copy()

while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

img_copy = img_copy[b:q, a:p]
cv2.imshow('cropped',img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
