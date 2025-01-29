#How to change resolution of our cam
import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
# set resolution HD(1280x720)
# cap.set(3,1280) # width
# cap.set(4,720) #height

def hd_resolution():
    cap.set(3, 1280)  # width
    cap.set(4, 720)  # height
    return cap
def sd_resolution():
    cap.set(3, 640)  # width
    cap.set(4, 480)  # height
    return cap
def FHD_resolution():
    cap.set(3, 1920)  # width
    cap.set(4, 1080)  # height
    cap.set(5,30)
    return cap
# to call hd_resolution function
# cap=hd_resolution()
# cap=sd_resolution()
cap=FHD_resolution()


while True:
    ret, frame=cap.read()
    if ret == True:
        cv.imshow('cam video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
