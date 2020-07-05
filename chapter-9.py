import cv2

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontface_default.xml")
img = cv2.imread("resources/biopic.jpg")
img = cv2.resize(img,(720,640))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow("Image",img)
cv2.waitKey(0)