import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('beach.jpg')
imgcopy = img.copy()
fig, (ax1, ax2) = plt.subplots( nrows=1, ncols=2, figsize= (20,20) )

#Drawing the circles
cv2.circle( imgcopy, center=(300,400), thickness=15, color=(255,0,0), radius=100 )

cv2.putText( imgcopy,  text="Tidewave", 
            org= (100,300),  
            color= (0,0,0), 
            thickness=5,
            fontFace = cv2.FONT_HERSHEY_DUPLEX, 
            fontScale = 2, 
            )

cv2.circle( imgcopy, center= (100,100), thickness=5, radius=20, color=(255,0,0) )
cv2.putText(imgcopy,
            org=(200,100),
            text="Hello",
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 1,
            thickness=10,
            color= (0,0,0),
            lineType = cv2.LINE_AA
            )
ax1.imshow( img)
ax2.imshow(imgcopy)
plt.show()