# In OpenCV, X and Y co-ordinates are a bit different,
# X = +X
# Y = -Y
# It means, the image or video lie in (X,-Y) plane

import cv2

img = cv2.imread("resources/biopic.jpg")
cv2.imshow("Image",img)
print(img.shape)

# Resize Images
imgResize = cv2.resize(img,(640,480))
cv2.imshow("Resized Image",imgResize)
print(imgResize.shape)

# Crop Images
imgcrop = img[240:830,:]
cv2.imshow("Cropped Image", imgcrop)

cv2.waitKey(0)