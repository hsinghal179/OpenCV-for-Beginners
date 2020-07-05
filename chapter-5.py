import cv2
import numpy as np

img = cv2.imread("resources/kings.jpg")
width,height = 250,350                                          # Size of Image Window
pts1 = np.float32([[325,57],[466,57],[325,267],[466,267]])      # Co-ordinates of club king
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)             
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)