#How to convert image from color to gray scale

import cv2 as cv
img=cv.imread("resources\mehdi.jpg")
img1=cv.resize(img,(800,600))
gray_img=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)


cv.imshow("dosri image",img1)
cv.imshow("tesri image",gray_img)

cv.waitKey(0) # wait for a key press
cv.destroyAllWindows() # close all OpenCV windows