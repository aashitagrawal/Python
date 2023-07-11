import cv2
import numpy as np
import time # for saved video in PC

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(r"C:\Users\aashi\Downloads\sam.mp4")
codec = cv2.VideoWriter_fourcc(*'XVID')
myVideo = cv2.VideoWriter('output.avi', codec, 24.0, (640,480)) # Here only original resolution of webcam will come

while True:
    ret,frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray_3ch = cv2.merge([img_gray, img_gray, img_gray]) #Making 3 channels
    img_gray_flipped = cv2.flip(img_gray_3ch, 1)
    myVideo.write(img_gray_flipped) #Here 3 channels photo will come
    cv2.imshow("webcam", img_gray_flipped)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    # time.sleep(1/20) # '20' is frame rate of uploaded video
cap.release()
myVideo.release()
cv2.destroyAllWindows()