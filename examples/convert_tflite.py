import ultralytics
ultralytics.checks()
from ultralytics import YOLO
model = YOLO('yolo11n.pt')
# model.export(format='tflite', imgsz=192, int8=True, no_post=False)
model.export(format='tflite', imgsz=224, int8=True, no_post=True)