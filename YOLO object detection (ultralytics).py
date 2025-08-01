# 14. YOLO object detection (ultralytics)
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.predict("image.jpg", show=True)
