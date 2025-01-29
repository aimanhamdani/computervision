import cv2 as cv
import numpy as np

img=np.zeros((600,600))
img1=np.ones((600,600))

#print size
print('the size of our canvas is', img.shape)
print(img)
#adding colors to the canvas
colored_img=np.zeros((600,600,3),np.uint8)
print('colored_image',colored_img.shape)
# print(colored_img)
#adding colors to the canvas complete image color
colored_img[:]=255,0,255

#color part of image
# colored_img[150:230,100:207]=255,0,0
# colored_img[-450:-370,-500:-393]=255,0,0
colored_img[100:200,100:200]=255,0,0
colored_img[100:200,400:500]=255,0,0
colored_img[250:300,300:320]=255,0,0
colored_img[400:450,200:400]=255,0,0
#adding line
cv.line(colored_img,(0,50),(550,600),(255,0,0),3)
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,150,200),3)
#to fill rectangle in place of thickness 3 put cv.filled
cv.rectangle(colored_img,(50,100),(300,400),(255,120,200),cv.FILLED)
cv.circle(colored_img,(400,300),50,(255,100,0),cv.FILLED)

# adding text
text = "I am learning\npython with Aamar"
lines = text.split('\n')

org = (200, 500)  # Starting position
font = cv.FONT_HERSHEY_DUPLEX
font_scale = 1
color = (255, 255, 0)
thickness = 2
line_height = 30  # Adjust line height according to your font size

for i, line in enumerate(lines):
    y = org[1] + i * line_height
    cv.putText(colored_img, line, (org[0], y), font, font_scale, color, thickness)

# cv.imshow('black',img)
# cv.imshow('white',img1)
cv.imshow('colored image',colored_img)
cv.waitKey(0)
cv.destroyAllWindows()