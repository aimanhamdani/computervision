#basic functions or manupulation in open cv
import cv2 as cv
import numpy as np
img=cv.imread("resources/mehdi.jpg")
#resize
img=cv.resize(img,(300,300))
#gray image
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#blur_img
blurr_img=cv.GaussianBlur(img,(23,23),0) #0 is kernel size, always 7,7 like odd becasue odd and odd make an image.
#edge detection
edge_img=cv.Canny(img,48,48)
#thickness of lines to change
mat_kernel= np.ones((7,7),np.uint8)
dilated_img=cv.dilate(edge_img,(mat_kernel),iterations=1)
#erosion: soil/sand ka apni jaga sa upar uth jana.
ero_img= cv.erode(dilated_img,(mat_kernel),iterations=1)
#black and white image
thresh,binary=cv.threshold(gray_img,152,255,cv.THRESH_BINARY)
#croping
print("the size of our image is: ",img.shape)
cropped_img=img[30:200,120:230]




cv.imshow('orignal',img)
cv.imshow('gray_img',gray_img)
cv.imshow('blurr_img',blurr_img)
cv.imshow('edge_img',edge_img)
cv.imshow('dilated_img',dilated_img)
cv.imshow('ero_img',ero_img)
cv.imshow('binary',binary)
cv.imshow('cropped image',cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()