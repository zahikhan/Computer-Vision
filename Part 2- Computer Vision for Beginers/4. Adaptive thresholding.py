import numpy as np
import matplotlib.pyplot as plt
import cv2

newspaper = cv2.imread("newspaper.png")
img = cv2.cvtColor(newspaper, cv2.COLOR_BGR2GRAY)

# Adaptive Thresholding
_ , thresh_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#_, thresh_binary = cv2.threshold(img, thresh = 127, maxval = 255, type = cv2.THRESH_BINARY)

adap_mean_2 =  cv2.adaptiveThreshold( img, 255, adaptiveMethod =  cv2.ADAPTIVE_THRESH_MEAN_C,  thresholdType = cv2.THRESH_BINARY ,  blockSize = 7 ,   C = 2 )
adap_mean_2_inv = cv2.adaptiveThreshold(img, 255,  cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 7, 2)
adap_mean_8 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 8)
adap_gaussian_8 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 8)

# Plot the images
images = [img, thresh_binary, adap_mean_2, adap_mean_2_inv, 
                        adap_mean_8, adap_gaussian_8]
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (15, 15))
for ind, p in enumerate(images):
                        ax = axs[ind%2, ind//2]
                        ax.imshow(p, cmap = 'gray')
                        ax.axis('off')
plt.show()