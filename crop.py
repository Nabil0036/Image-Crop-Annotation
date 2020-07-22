import cv2
import numpy as np
import os
import time
import argparse

p1,p2 =tuple(),tuple()
i=0

a = argparse.ArgumentParser()
a.add_argument("-i", "--image", required=True, help="Path to the images that needed to be cropped")
a.add_argument("-c", "--cropped", required=True, help="Path to where cropped images are stored")
args = vars(a.parse_args())

image_path = args["image"]

def call_back_func(event, x, y, flags, param):    
    global p1,p2,i,roi
    if event == cv2.EVENT_LBUTTONDOWN:
        p1 = (x,y)
        print("tipe rakhse",x,"  ",y)
    elif event == cv2.EVENT_LBUTTONUP:
        p2 = (x,y)
        print("chere rakhse",x,"  ",y)
        try:
            roi = img[p1[1]:p2[1],p1[0]:p2[0]]
            cv2.imshow('cropped',roi)
        except:
            roi = img[p2[1]:p1[1],p2[0]:p1[0]] 
            cv2.imshow('cropped',roi)
        pa = os.path.join(args["cropped"],"",str(i)+'.jpg')
        pa = pa.replace("/","\\")
        print(pa)
        cv2.imwrite(pa,roi)
        
images = os.listdir(image_path)

while i<len(images):
    im_path =images[i]
    img = cv2.imread("images\\"+im_path)
    k = cv2.waitKey(33)
    cv2.imshow('image',img)
    if k == ord('a'):
        cv2.destroyWindow('cropped')
        i+=1
    cv2.setMouseCallback('image',call_back_func)
    

cv2.waitKey(0)
cv2.destroyAllWindows()
