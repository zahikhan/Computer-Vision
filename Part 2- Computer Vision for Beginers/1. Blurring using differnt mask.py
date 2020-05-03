import cv2
import  numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("NYtimes.jpg")
img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB)

#Kernel

Kernel = [ 1, 5 ,  7 , 11 ]

fig , axs = plt.subplots( nrows =1 , ncols =4, figsize = (20,20) )

for loop, fvalue in enumerate(Kernel):
            ax =  axs[loop]
            img_blurred = cv2.blur(img, ksize=(fvalue, fvalue))
            ax.imshow(img_blurred)
            ax.axis('off')

ax.imshow(img)
plt.show()