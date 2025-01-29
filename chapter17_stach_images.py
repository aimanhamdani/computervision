import cv2 as cv
import numpy as np
img=cv.imread(r"resources\certificate_nebosh.jpg")
img=cv.resize(img,(500,300))
img1=cv.imread(r"resources\bhagat_singh.jpg")
img1=cv.resize(img1,(img.shape[1],img.shape[0]))


print(img.shape)
print(img1.shape)
#how to join,stack images
hor_img=np.hstack((img,img1))
ver_img=np.vstack((img,img1))


# cv.imshow('hstack',hor_img)
cv.imshow('vstack',ver_img)


cv.waitKey(0)

cv.destroyAllWindows()