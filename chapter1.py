#how to show the image
import cv2 as cv
img=cv.imread("resources\mehdi.jpg")
cv.imshow("pehli image",img)
# wait
cv.waitKey(0) # wait for a key press
cv.destroyAllWindows()
