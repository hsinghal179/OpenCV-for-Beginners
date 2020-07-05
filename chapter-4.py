import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)   # Black image of 512x512 pixels with 3 layers of colours(B,G,R)
img[:] = 0,255,0                       # Colour to all pixels
cv2.line(img,(0,0),(256,256),(0,0,255),5)
cv2.rectangle(img,(256,0),(512,256),(255,0,0),5)
cv2.circle(img,(256,256),100,(0,0,0),10)
cv2.putText(img,"Open CV",(120,480),cv2.FONT_ITALIC,2,(0,0,0),1)
cv2.imshow("Image",img)

cv2.waitKey(0)