#How to change resolution of our cam
import cv2 as cv
import numpy as np
import time

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
cap=hd_resolution()
# cap=sd_resolution()
# cap=FHD_resolution()

# Video ki properties hasil karein
width = int(cap.get(3))
height = int(cap.get(4))
fps=int(cap.get(5))
delay = 1/fps


# VideoWriter object create karein
fourcc = cv.VideoWriter_fourcc('M','J','P','G')
out = cv.VideoWriter('resources/output_webcam.avi', fourcc, fps, (width, height))

while True:
    start_time=time.time()

    ret, frame = cap.read()
    if ret == True:
        # gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        # thresh,binary=cv.threshold(gray_frame,155,255,cv.THRESH_BINARY)
        # out.write(binary)
        # out.write(gray_frame)
        out.write(frame)
        # cv2.imshow('binary', binary)
        # cv2.imshow('gray',gray_frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    end_time=time.time()
    elapsed_time=end_time-start_time
    if elapsed_time<delay:
        time.sleep(delay-elapsed_time)

# Resources release karein
cap.release()
out.release()
cv.destroyAllWindows()
print("Program khatam.")
