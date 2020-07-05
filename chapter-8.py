import cv2
import numpy as np

def getContours(img):
    contours, heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if(area>500):
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x,y,h,w = cv2.boundingRect(approx)

            if objCor == 3:
                shapeType = "Tri"
            elif objCor == 4:
                shapeType = "Quad"
            elif objCor == 5:
                shapeType = "Penta"
            elif objCor == 6:
                shapeType = "Hexa"
            else:
                shapeType = "Circle"
            cv2.rectangle(imgContour,(x,y),(x+h,y+w),(0,255,0),2)
            cv2.putText(imgContour,shapeType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_ITALIC,0.8,(0,0,0),2)

path = 'resources/shapes.jpg'
img = cv2.imread(path)
img = cv2.resize(img,(300,300))
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)

imgS1 = np.hstack((imgGray,imgBlur,imgCanny))
imgS2 = np.hstack((img,imgBlank,imgContour))
cv2.imshow("Stack Image",imgS1)
cv2.imshow("Stack Image Main",imgS2)
cv2.waitKey(0)