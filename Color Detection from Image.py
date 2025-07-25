import cv2

def detect_color(image_path, x, y):
    img = cv2.imread(image_path)
    b, g, r = img[y, x]
    print(f"RGB at ({x},{y}): R={r}, G={g}, B={b}")
    
detect_color("image.jpg", 50, 100)
