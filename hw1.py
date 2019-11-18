import cv2
import numpy as np
img=cv2.imread("aaa.jpg")
cv2.imshow("aaa",img)
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
width=492
height=689
size=(width,height)
video= cv2.VideoWriter("hw1.avi",fourcc,2,size)
#matrix=np.zeros((height,width,3),np.uint8)
#matrix.fill(255)
img=cv2.putText(img,'3160102215SUMAN',(50,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,0,0),2)
for i in range(1,10):
	video.write(img)
video.release()