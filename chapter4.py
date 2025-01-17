#How to convert image from gray scale to binary
import cv2 as cv
# Load the image
img=cv.imread("resources\mehdi.jpg")
# show orignal image
cv.imshow('orignal image',img)
# Convert the image to grayscale
gray_scale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_scale image',gray_scale)
# convert the image from grayscale to binary
thresh,binary=cv.threshold(gray_scale,127,255,cv.THRESH_BINARY)
cv.imshow('binary image',binary)
cv.waitKey(0)
cv.destroyAllWindows()