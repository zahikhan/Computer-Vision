import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('walloflove.jpg')
imgcopy = img.copy()
fig, (ax1, ax2) = plt.subplots( nrows=1, ncols=2, figsize= (20,20) )

cv2.circle( imgcopy, center=(300,400), thickness=15, color=(255,0,0), radius=100 )

ax1.imshow( img)
ax2.imshow(imgcopy)
plt.show()