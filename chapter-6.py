import cv2
import numpy as np

im = cv2.imread("resources/biopic.jpg")
img = im[240:730,450:930]
img = cv2.resize(img,(250,250))

imgHor = np.hstack((img,img))
imgVer = np.vstack((imgHor,imgHor,imgHor))

cv2.imshow("Image",imgVer)

cv2.waitKey(0)