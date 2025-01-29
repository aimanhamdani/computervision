import cv2
import numpy as np

# Create a video capture object
cap = cv2.VideoCapture(0)

# Video ki properties hasil karein
width = int(cap.get(3))
height = int(cap.get(4))


# VideoWriter object create karein
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('resources/output_webcam.avi', fourcc, 30, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    thresh,binary=cv2.threshold(gray_frame,155,255,cv2.THRESH_BINARY)
    # out.write(binary)
    # out.write(gray_frame)
    out.write(frame)
    # cv2.imshow('binary', binary)
    # cv2.imshow('gray',gray_frame)
    cv2.imshow('frame',frame)

    
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# Resources release karein
cap.release()
out.release()
cv2.destroyAllWindows()
print("Program khatam.")
