import cv2

video = cv2.VideoCapture(0)
first_frame = None

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if first_frame is None:
        first_frame = gray
        continue
    
    delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)[1]
    
    if thresh.sum() > 5000000:
        print("Motion Detected!")
        
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
