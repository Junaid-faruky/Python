import cv2
import numpy as np

cap = cv2.VideoCapture(0)
bg = None

while True:
    ret, frame = cap.read()
    if not ret: break
    
    if bg is None:
        bg = frame
        continue
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2

    frame[np.where(mask==255)] = bg[np.where(mask==255)]
    cv2.imshow("Cloak", frame)

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
