import cv2
import numpy as np

flag=False
curr_x = -1
curr_y = -1

def draw(event, x, y, flags, parameters):
    global flag, curr_x, curr_y
    if event==1:
        flag = True
        curr_x = x
        curr_y = y
    elif event==0:
        if flag:
            cv2.rectangle(img, pt1=(curr_x,curr_y), pt2=(x,y), color=(255,255,255), thickness=-1)
    elif event==4:
        flag = False
        cv2.rectangle(img, pt1=(curr_x, curr_y), pt2=(x,y), color=(255,0,255), thickness=-1)

cv2.namedWindow(winname="rectangle")
cv2.setMouseCallback("rectangle", draw)

img = np.zeros((500,500,3))

while True:
    cv2.imshow("rectangle",img)
    if (cv2.waitKey(1) & 0xFF) == ord('x'):
        break
cv2.destroyAllWindows()