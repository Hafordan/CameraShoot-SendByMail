import cv2

Camera = cv2.VideoCapture(0)

if not Camera.isOpened():
    exit()

ret, frame = Camera.read()

cv2.imwrite('Camera.jpg', frame)

Camera.release()
import SendByMail