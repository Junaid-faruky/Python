import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img = cv2.imread("people.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    face = img[y:y+h, x:x+w]
    face = cv2.GaussianBlur(face, (99, 99), 30)
    img[y:y+h, x:x+w] = face

cv2.imwrite("blurred_faces.jpg", img)
print("Faces blurred!")
