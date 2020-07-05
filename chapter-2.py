import cv2
import numpy as np

img = cv2.imread("resources/biopic.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                # For gray Image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)                    # For Blur Image
imgCanny = cv2.Canny(img,150,200)                              # For Black & White Sketched Image
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)       # For increasing thickness of Edges of Image
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)        # For decreasing thickness of Edges of Image

cv2.imshow("Output 1",imgGray)
cv2.imshow("Output 2",imgBlur)
cv2.imshow("Output 3",imgCanny)
cv2.imshow("Output 4",imgDialation)
cv2.imshow("Output 5",imgEroded)
cv2.waitKey(0)