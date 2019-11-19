import cv2

global flag
flag=False

def mouse_event(event, x, y, flags, param):
	global flag
	if event == cv2.EVENT_LBUTTONDOWN:
		flag=True;
	elif event == cv2.EVENT_MOUSEMOVE:
		if flag:
			cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
	elif event == cv2.EVENT_LBUTTONUP:
		flag=False;


img=cv2.imread("aaa.jpg")
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
width=492
height=689
size=(width,height)
video= cv2.VideoWriter("hw1.avi",fourcc,6,size)

img=cv2.putText(img,'3160102215SUMAN',(50,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,0,0),2)
for i in range(1,7):
	video.write(img)
	cv2.imshow('frame',img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)

for i in range(1,10):
	cv2.circle(img,(0,0),i*100,(255,255,255),-1)
	video.write(img)
	cv2.imshow('frame',img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_event)
img=cv2.putText(img,'click mouse to start',(50,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,0,0),2)
img=cv2.putText(img,'push SPACE to stop painting',(50,400),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,0,0),2)
while(1):
	cv2.imshow('frame',img)
	video.write(img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		break;

for i in range(1,10):
	cv2.rectangle(img,(450-50*i,0),(500,700),(166,215,166),-1)
	cv2.imshow('frame',img)
	video.write(img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)

for i in range(1,3):
	cv2.circle(img,(250,250),70,(0,0,255),5)
	cv2.imshow('frame',img)
	video.write(img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)
for i in range(1,3):
	cv2.line(img,(250,100),(250,400),(0,0,255),5)
	cv2.imshow('frame',img)
	video.write(img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)
for i in range(1,3):
	cv2.line(img,(150,400),(350,400),(0,0,255),5)
	cv2.imshow('frame',img)
	video.write(img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)

for k in range(1,6):
	for i in range( height ):
		for j in range( width - k*100 ):
			img[i, j] = img[i, j+100]
	cv2.imshow('frame',img)
	video.write(img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)

for i in range(1,7):
	if flag:
		img=cv2.putText(img,'FIN',(width/2,height/2),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(255,0,0),2)
	else:
		img=cv2.putText(img,'FIN',(width/2,height/2),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,0,255),2)
	
	flag = bool(1-flag)
	cv2.imshow('frame',img)
	video.write(img)
	if(cv2.waitKey(100)&0xFF==ord(' ')):
		cv2.waitKey(0)

video.release()
