import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread( 'walloflove.jpg' )
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgcopy = img.copy()

#Draw a rectangle
cv2.rectangle( imgcopy, pt1=(100,400), pt2=(600,600), thickness=20, color=(255,0,0))

#Draw a rectangle
#cv2.rectangle( imgcopy, pt1= (800,800), pt2 =(1000,1000), color=(255,0,0), thickness=15 )

fig , (p1, p2) = plt.subplots( nrows= 1 , ncols=2, figsize = (20,20) )

p1.imshow(imgcopy)
p2.imshow(img)
plt.show()