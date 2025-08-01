# 18. Face detection with OpenCV
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
img = cv2.imread("face.jpg")
faces = face_cascade.detectMultiScale(img,1.1,4)
print("Faces found:", len(faces))
