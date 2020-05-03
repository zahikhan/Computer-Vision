import cv2
import  numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("gradient.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Thresholding 
_ , thresh_0 = cv2.threshold( img , 127, 255,  cv2.THRESH_BINARY )
_ , thresh_1 = cv2.threshold( img , 127, 255,  cv2.THRESH_BINARY_INV )
_ , thresh_2 = cv2.threshold( img , 127, 255,  cv2.THRESH_TOZERO )
_ , thresh_3 = cv2.threshold( img , 127, 255,  cv2.THRESH_TOZERO_INV )
_ , thresh_4 = cv2.threshold( img , 127, 255,  cv2.THRESH_TRUNC )
# Plot the images
images = [img, thresh_0, thresh_1, thresh_2, thresh_3, thresh_4]
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (13, 13))
for ind, p in enumerate(images):
    ax = axs[ind//3, ind%3]
    ax.imshow(p, cmap='gray')
plt.show()
