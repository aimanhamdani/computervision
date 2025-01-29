import cv2 as cv
cap=cv.VideoCapture(0)

ret,frame=cap.read()
while True:
    
    if ret == False:
        print('no webcam found')
        break
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    thresh,binary=cv.threshold(gray_frame,127,255, cv.THRESH_BINARY)
    cv.imshow('binary',binary)
    cv.imshow('orignal',frame)
    cv.imshow('gray_scale',gray_frame)
    if cv.waitKey(1) & 0xFF== ord('q'):

        break
cap.release()
cv.destroyAllWindows()
    