#how to resize the image
import cv2 as cv
img=cv.imread("resources\mehdi.jpg")
img1=cv.resize(img,(400,300))
cv.imshow("pehli image",img)
cv.imshow("dosri image",img1)

cv.waitKey(0) # wait for a key press
cv.destroyAllWindows() # close all OpenCV windows