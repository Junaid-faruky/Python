import cv2

cam = cv2.VideoCapture(0)
ret, frame = cam.read()
cv2.imwrite("snapshot.jpg", frame)
cam.release()
