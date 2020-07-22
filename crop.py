import cv2
import numpy as np
import os
import time

p1,p2 =tuple(),tuple()
image_path = ".\images"
i=0
def call_back_func(event, x, y, flags, param):
    
    global p1,p2,i,roi
    if event == cv2.EVENT_LBUTTONDOWN:
        p1 = (x,y)
        print("tipe rakhse",x,"  ",y)
    elif event == cv2.EVENT_LBUTTONUP:
        p2 = (x,y)
        print("chere rakhse",x,"  ",y)
        roi = img[p1[1]:p2[1],p1[0]:p2[0]] 
        cv2.imshow('ruki',roi)
        cv2.imwrite("D:\\image_cropper\\corped_images\\"+str(i)+".jpg",roi)
        
    
    


images = os.listdir(image_path)

while i<len(images):
    im_path =images[i]
    img = cv2.imread("images\\"+im_path)
    k = cv2.waitKey(33)
    cv2.imshow('image',img)
    if k == ord('a'):
        #black = np.zeros((512,512,3),np.uint8)
        #cv2.imshow('ruki',black)
        cv2.destroyWindow('ruki')
        i+=1
    cv2.setMouseCallback('image',call_back_func)
    

cv2.waitKey(0)
cv2.destroyAllWindows()
