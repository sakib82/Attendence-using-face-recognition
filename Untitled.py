#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
print(cv2.__version__)
fo = open("input.txt","r")
# print("Opening input file.......",fo.name)

from PyQt5.Qt import PYQT_VERSION_STR
print("PyQt version:", PYQT_VERSION_STR)

print("File name : ",fo.name)
print("Open or closed : ",fo.closed)
print("Opening mode : ",fo.mode)
# print("Softspace flag : ", fo.softspace)


# In[13]:


import cv2

import os
dir_path = os.getcwd() # current directory
print(dir_path)
camera = cv2.VideoCapture(0)
cv2.namedWindow("Camera test")

i = 0
imgpath = "C:/Users/Sakib/Desktop/New/"
name = 'image' + str(i) + '.png'

for i in range(4):
	return_value, image = camera.read()
	cv2.imwrite(os.path.join(imgpath,name),image)
#   cv2.imwrite(os.path.join(path,imgpath+'opencv' + str(i) + '.png'),image)
# 	cv2.imshow(os.path.join(path,"Capturing image  : ",image)
	i = i+1
    
cv2.waitKey(0)
cv2.destroyWindow("Camera test")
del(camera)


# # Run webcam, take photo and store in a pre-specified directory (Successful)
# Name : Train

# In[1]:


import cv2
import os

dir_path = os.getcwd() # current directory
print("Current directory : " , dir_path)

camera = cv2.VideoCapture(0)
cv2.namedWindow("Camera test")

i = 0
img_num = 15
imgpath = "C:/Users/Sakib/Desktop/New/"

print(" Images are being taken ............." )
for i in range(img_num+1):
	name = 'train' + str(i) + '.png'
	return_value, image = camera.read()
	cv2.imwrite(os.path.join(imgpath,name),image)
	cv2.imshow("Camera test",image)
#   cv2.imwrite(os.path.join(path,imgpath+'opencv' + str(i) + '.png'),image)
# 	cv2.imshow(os.path.join(path,"Capturing image  : ",image)
	i = i+1
cv2.waitKey(0)
cv2.destroyWindow("Camera test")
del(camera)
print("............ COMPLETE ................" )


# # Run face detection in those taken photoes(Successful)
# Name : Face Detect // ( next : face recognition) ( separate framed faces from the video )

# In[27]:


import cv2
import os


cascade_path = "C:/Users/Sakib/Desktop/haarcascade_frontalface_default.xml"
facecascade = cv2.CascadeClassifier(cascade_path)

img_num = 5

for i in range(1,img_num+1):
	name = 'train' + str(i) + '.png'
	image_path = "C:/Users/Sakib/Desktop/New/"
	image_name = image_path+name
	print(image_path+name)
    
	image = cv2.imread(image_name)
	image = cv2.resize(image,(800,600))
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	faces = facecascade.detectMultiScale(gray,scaleFactor = 1.3,
                                    minNeighbors=2,
                                    minSize=(10,10),
                                    flags = cv2.CASCADE_SCALE_IMAGE)
# cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])

	print("Found {0} faces.".format(len(faces)))


	for(x,y,w,h) in faces:
		cv2.rectangle(image,(x,y),(x+w, y+h),(0,255,0),2)

	cv2.imshow(name,image)
	cv2.waitKey(0)
	cv2.destroyWindow(name)


# # select a image and detect faces in that image(Successful)

# In[18]:


import cv2
import os

imagepath = "C:/Users/Sakib/Desktop/test2.jpg"
cascadpath = "C:/Users/Sakib/Desktop/haarcascade_frontalface_default.xml"

facecascade = cv2.CascadeClassifier(cascadpath)

image = cv2.imread(imagepath)
image = cv2.resize(image,(800,600))
# cv2.imshow("OK?",image)
# cv2.waitKey(0)
# cv2.destroyWindow("OK?")
# image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = facecascade.detectMultiScale(gray,scaleFactor = 1.3,
                                    minNeighbors=2,
                                    minSize=(10,10),
                                    flags = cv2.CASCADE_SCALE_IMAGE)
# cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
print("Found {0} faces.".format(len(faces)))


for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(0,255,0),2)

cv2.imshow("Faces Found",image)
cv2.waitKey(0)
cv2.destroyWindow("Faces Found")


# # Detect faces in Video (successful)

# In[ ]:


import cv2

cap = cv2.VideoCapture(0)

cascadpath = "C:/Users/Sakib/Desktop/haarcascade_frontalface_default.xml"
facecascade = cv2.CascadeClassifier(cascadpath)


while(True):
    ret, frame = cap.read()
    faces = facecascade.detectMultiScale(gray,scaleFactor = 1.3,
                                    minNeighbors=2,
                                    minSize=(10,10),
                                    flags = cv2.CASCADE_SCALE_IMAGE)
    
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)

    cv2.imshow('frame',frame) #cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

