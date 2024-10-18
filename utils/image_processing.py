import cv2
import numpy as np

def detect_red_objects(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    blurred = cv2.GaussianBlur(red_mask, (5, 5), 0)
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_objects = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1000:
            continue
        perimeter = cv2.arcLength(cnt, True)
        if perimeter == 0:
            continue
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
        M = cv2.moments(cnt)
        if M['m00'] == 0:
            continue
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        shape = classify_shape(approx, cnt)
        if shape in ['Triangle', 'Square', 'Rectangle', 'Circle']:
            detected_objects.append({
                'position': (cx, cy),
                'shape': shape,
                'contour': cnt
            })
    return detected_objects

def classify_shape(approx, contour):
    num_vertices = len(approx)
    shape = 'Unknown'
    if num_vertices == 3:
        shape = 'Triangle'
    elif num_vertices == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        if 0.95 <= aspect_ratio <= 1.05:
            shape = 'Square'
        else:
            shape = 'Rectangle'
    elif num_vertices > 4:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        if perimeter == 0:
            return 'Unknown'
        circularity = 4 * np.pi * (area / (perimeter * perimeter))
        if circularity > 0.75:
            shape = 'Circle'
        else:
            shape = 'Unknown'
    else:
        shape = 'Unknown'
    return shape
