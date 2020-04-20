import numpy as np
import matplotlib.pyplot as plt 
import cv2

#READING THE Image as BGR
img = cv2.imread('beach.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray, cmap= 'gray')   # SHOWING IMAGE AS RGB      
plt.show()              

