import cv2
import numpy as np

# cv2.waitKey(0) #This return the ASCII code of any key pressed in waiting time, if none is pressed it reutrns -1
# print(ord('x')) #This prints the ASCII code of specified letter
# print(0xFF) # Prints decimal numbers, after converting 0xFF (hexadecimal) to decimal


def draw(event, x, y, flags, parameters):
    # if event==0:
    #     print("Mouse Moved")
    if event==1:
        print("Mouse down clicked")
        cv2.circle(img, center=(x,y), radius=30, color=(255,255,0), thickness=-1)
    if event==4:
        print("Mouse up clicked")
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print("Double click")        
    
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)

img = np.zeros((500,500,3))

while True:
    cv2.imshow("window", img)
    if (cv2.waitKey(1) & 0xFF) == ord('x'):
        break
cv2.destroyAllWindows()
