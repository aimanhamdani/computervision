#import libraries to capture webcam.
import cv2 as cv
import numpy as np
#step2 
cap=cv.VideoCapture(0) #webcam no.
#step3 display frame by frame
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #to display frame
        cv.imshow('frame', frame)
    #to quit with q key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
                  
#to release or close windows easily.
cap.release()
cv.destroyAllWindows()

