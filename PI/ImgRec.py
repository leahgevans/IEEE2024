import cv2
import argparse
import supervision as sv

from ultralytics import YOLO
CAM_1 = 0

cam = cv2.VideoCapture(CAM_1)

model = YOLO("best (2).pt")

# box_ann = sv.BoxAnnotator(thickness = 2, text_thickness = 2, text_scale = 1)

def isDetectingBox():
    ret, frame = cam.read()

    result = model(frame)[0]
    box = False
    detections = sv.Detections.from_yolov8(result)
    if(detections):
        box = True
    return box
    
    
# detections = sv.Detections.from_yolov8(result)
# # labels = [
# #     f"{model.model.names[class_id]}"
# #     for _, class_id, _
# #     in detections
# # ]
# frame = box_ann.annotate(scene=frame, detections = detections) #, labels = labels)

# cv2.imshow('yolov8', frame)
# if(cv2.waitKey(30) == 27):
#     break
