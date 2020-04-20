import numpy as np
import matplotlib.pyplot as plt
import cv2

# Step 1. Define callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, center = (x, y), radius = 5, 
                       color = (87, 184, 237), thickness = -1)
    elif event == cv2.EVENT_RBUTTONDOWN:        
            cv2.circle(img, center = (x, y), radius = 10,  
                       color = (87, 184, 237), thickness = 1)
img = cv2.imread('map.jpg')
cv2.namedWindow(winname = 'Map')
cv2.setMouseCallback('Map', draw_circle)

# Step 3. Execution
while True:
    cv2.imshow('Map',img)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()