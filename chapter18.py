#coordinates of an image or video
#step-1 import libraries
import cv2 as cv
import numpy as np

#step-2 define a function
def find_coord(event,x,y,flag,param):
    if event == cv.EVENT_LBUTTONDOWN:
        #left mouse click
        print(x,",",y)
        #how to define or print on the same image or window
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x)+','+str(y),(x,y),font,1,(0,0,0),thickness=2)
        #show the text on image annd img itself
        cv.imshow('image',img)
    # for color finding
    if event == cv.EVENT_MBUTTONDOWN:
        

        font=cv.FONT_HERSHEY_SIMPLEX
        b= img[y,x,0]
        g= img[y,x,1]
        r= img[y,x,2]
        print(b,',',g,',',r)
        cv.putText(img, str(b)+ ',' + str(g)+ ',' + str(r), (x, y), font, .5, (255 , 255 , 255),2)
        cv.imshow('image', img)


#find function to read and display

if __name__=="__main__":
    #reading an image
    img=cv.imread(r'resources\bhagat_singh.jpg')
    #display the image
    cv.imshow('image',img)
    #setting call back function
    cv.setMouseCallback('image',find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()

