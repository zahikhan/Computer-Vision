import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('beach.jpg')
#Converting the image into HSL  and HSV 

# Transform the image into HSV and HLS models
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
# Plot the converted images
fig, (ax1, ax2,ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (20, 20))
ax1.imshow(img_hsv)
ax2.imshow(img_hls)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ax3.imshow(img )
plt.show()
