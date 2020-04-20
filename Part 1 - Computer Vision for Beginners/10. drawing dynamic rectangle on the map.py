import numpy as np
import matplotlib.pyplot as plt
import cv2
drawing = False
ix = -1
iy = -1
def myposition(event, x,y,flags, param):
            global drawing , ix ,   iy        
            if event == cv2.EVENT_LBUTTONDOWN:
                         ix = x 
                         iy = y
                         drawing = True
            elif event == cv2.EVENT_MOUSEMOVE:
                        if drawing == True:
                                cv2.rectangle(img, pt1=(ix, iy), pt2=(x,y), color=(87,184,237), thickness= -1 )
            elif event == cv2.EVENT_LBUTTONUP:
                                                drawing = False
                                                cv2.rectangle(img, pt1=(ix, iy), pt2=(x,y), color=(87,184,237), thickness= -1 )

img = cv2.imread('map.jpg')
cv2.namedWindow(winname= 'Map')
cv2.setMouseCallback('Map', myposition)

while True:
            cv2.imshow('Map',img)
            if cv2.waitKey(10) & 0xFF == 27:
                        break

