#How to save an image
import cv2 as cv
# Load the image
img=cv.imread('resources\mehdi.jpg')
#convert to gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#covert gray to binary
thresh,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)
binary=cv.resize(binary,(400,200))
#how to save an image
cv.imwrite('resources/mehid_gray.png',gray)
cv.imwrite('resources/binary_mehdi.png',binary)