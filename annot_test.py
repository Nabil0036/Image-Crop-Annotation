import pickle
import cv2
import argparse

a = argparse.ArgumentParser()
a.add_argument("-a","--annotations",required=True, help="Path to the annotations file")
args = vars(a.parse_args())

f = open(args["annotations"], 'rb')
data = pickle.load(f)
f.close()

def imshow(tup):
    img = tup[0]
    x1,y1,x2,y2 = tup[1],tup[2],tup[3],tup[4]
    img = cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,0), 2) 
    cv2.imshow("image",img)


i=0
while i<len(data):
    d = data[i]
    imshow(d)
    k = cv2.waitKey(33)
    if k == ord('a'):
        i+=1

#cv2.waitKey(0)
cv2.destroyAllWindows()