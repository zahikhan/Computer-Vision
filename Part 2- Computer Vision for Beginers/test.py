import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("gradient.jpg")
_ , thres_0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)           #Convert image into binary and if(X,Y) > 127 then white else black
_ , thres_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) #Inverse binary thresholded image

_ , thres_2 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_ , thres_3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
_, thres_4 = cv2.threshold(img , 127, 255 , cv2.THRESH_TRUNC)


images = [ thres_0, thres_1, thres_2, thres_3, thres_4 ]
fig, axs = plt.subplots(nrows=2, ncols=3, figsize = (20,20) )
for axis, image in enumerate(images):
            ax =  axs[axis/3, axis%3]
            ax.imshow(image)
plt.show()
