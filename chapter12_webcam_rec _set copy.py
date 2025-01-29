import cv2 as cv
import numpy as np

# Create a video capture object
cap = cv.VideoCapture(0)
cap.set(10,100)
cap.set(3,640)
cap.set(4,480)

# cap.set()
while True:
    ret,frame=cap.read()
    if ret ==True:
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()

