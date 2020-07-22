import cv2
import numpy as np
import os
import time
import pickle
import argparse

a = argparse.ArgumentParser()
a.add_argument("-i", "--image", required=True, help="Path to the images that needed to be cropped")
a.add_argument("-a", "--annotations", required=True, help="Path to where annotating image and bounding box saved")
args = vars(a.parse_args())


p1,p2 =tuple(),tuple()
image_path = args["image"]
i=0

images_and_annotations =[]
def call_back_func(event, x, y, flags, param):
    
    global p1,p2,i,roi
    if event == cv2.EVENT_LBUTTONDOWN:
        p1 = (x,y)
        print("tipe rakhse",x,"  ",y)
    elif event == cv2.EVENT_LBUTTONUP:
        p2 = (x,y)
        print("chere rakhse",x,"  ",y)
        roi = img[p1[1]:p2[1],p1[0]:p2[0]]
        x1 ,y1,x2,y2 =  p1[0],p1[1],p2[0],p2[1]
        cv2.imshow('ruki',roi)
        cv2.imwrite("D:\\image_cropper\\corped_images\\"+str(i)+".jpg",roi)
        tup = (img,x1,y1,x2,y2)
        images_and_annotations.append(tup)
    
    


images = os.listdir(image_path)

while i<len(images):
    im_path =images[i]
    pa= os.path.join(args["image"],im_path)
    img = cv2.imread(pa)
    k = cv2.waitKey(33)
    cv2.imshow('image',img)
    if k == ord('a'):
        #black = np.zeros((512,512,3),np.uint8)
        #cv2.imshow('ruki',black)
        cv2.destroyWindow('ruki')
        i+=1
    cv2.setMouseCallback('image',call_back_func)

f = open(args["annotations"], 'wb')
 
pickle.dump(images_and_annotations,f)
f.close()
cv2.waitKey(0)
cv2.destroyAllWindows()
