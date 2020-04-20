import numpy as np
import matplotlib.pyplot as plt 
import cv2

#READING THE Image as BGR
img = cv2.imread('beach.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)   # SHOWING IMAGE AS RGB      
plt.show()              

