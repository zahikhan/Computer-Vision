import cv2
import  numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("NYtimes.jpg")
img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB)

average = cv2.blur(img, ksize = (5, 5))                     #Uses average filter mask
median = cv2.medianBlur( img, 3)                #Same as average but uses median(middle)
gussian = cv2.GaussianBlur(img, ksize=(5,5), sigmaX=0 )     #Smooths entire in fourier 
bilteral = cv2.bilateralFilter(img, 7, sigmaSpace =75, sigmaColor = 75 )            #Keeps edges sharp advanced version of gaussian
#takes care of pixels location and color.

images = [average, median, gussian, bilteral]
fig, axs =  plt.subplots(nrows=1, ncols=4 , figsize = (30,30))

for index, p in enumerate(images):
            ax= axs[index]
            ax.imshow(p)
            ax.axis('off')
            

plt.show();
