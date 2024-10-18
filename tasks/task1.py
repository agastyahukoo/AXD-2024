# tasks/task1.py

import cv2
from utils.image_processing import detect_red_objects
from utils.centroid_tracker import CentroidTracker

def run():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open video capture.")
        return
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('task1_output.avi', fourcc, 20.0, (frame_width, frame_height))
    ct = CentroidTracker(maxDisappeared=10, maxDistance=50)
    counts = {'Triangle': 0, 'Square': 0, 'Rectangle': 0, 'Circle': 0}
    countedObjectIDs = set()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detected_objects = detect_red_objects(frame)
        detections = []
        for obj in detected_objects:
            centroid = obj['position']
            shape = obj['shape']
            detections.append((centroid, shape))
        objects = ct.update(detections)
        for (objectID, (centroid, shape)) in objects.items():
            text = f"ID {objectID}: {shape}"
            cv2.putText(frame, text, (centroid[0] - 50, centroid[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
            if objectID not in countedObjectIDs and shape in counts:
                counts[shape] += 1
                countedObjectIDs.add(objectID)
        y_offset = 30
        for shape_key, count in counts.items():
            text = f"{shape_key}s: {count}"
            cv2.putText(frame, text, (10, y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            y_offset += 30
        out.write(frame)
        cv2.imshow('Task 1 - Shape Detection and Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
