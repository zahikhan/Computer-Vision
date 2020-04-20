import numpy as np
import matplotlib.pyplot as plt 
import cv2

#READING THE Image as BGR
img = cv2.imread('beach.jpg')
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Plot the three channels of the image
fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize = (20, 20))

for loop in range(0,3):
            ax  = axs[loop];
            ax.imshow( img[ : , : ,loop], cmap= 'gray' )   # SHOWING IMAGE AS RGB      
plt.show()              

