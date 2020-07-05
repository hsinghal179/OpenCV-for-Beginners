import cv2

# Image scan
img = cv2.imread("resources/biopic.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)

# Video Scan
cap = cv2.VideoCapture("resources/sampleVideo.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Camera Scan
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)        # For mirror video capture
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break