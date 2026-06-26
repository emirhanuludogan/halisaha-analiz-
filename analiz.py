from ultralytics import YOLO
import cv2
import numpy as np
import csv

model = YOLO('yolo11n.pt')
cap = cv2.VideoCapture("kesi2t.mp4")

log_file = open('oyuncu_takip.csv', 'w', newline='')
csv_writer = csv.writer(log_file)
csv_writer.writerow(['Frame', 'ID', 'X', 'Y'])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    results = model.track(frame, persist=True, tracker="botsort.yaml")
    annotated_frame = results[0].plot()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sharp = cv2.filter2D(gray, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
    thresh = cv2.adaptiveThreshold(sharp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv, (30, 40, 40), (90, 255, 255))
    field_edges = cv2.bitwise_and(thresh, thresh, mask=green_mask)
    
    field_edges = cv2.dilate(field_edges, np.ones((3,3), np.uint8), iterations=1)
    lines = cv2.HoughLinesP(field_edges, 1, np.pi/180, 50, minLineLength=120, maxLineGap=40)

    combined = cv2.addWeighted(annotated_frame, 1.0, cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR), 0.2, 0)

    if results[0].boxes:
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = int((x1 + x2) / 2), y2 
            
            obj_id = int(box.id[0]) if box.id is not None else 0
            
            csv_writer.writerow([int(cap.get(cv2.CAP_PROP_POS_FRAMES)), obj_id, cx, cy])
            
            cv2.circle(combined, (cx, cy), 5, (0, 0, 255), -1)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(combined, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow("Analiz ve Cizgi Takibi", combined)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

log_file.close()
cap.release()
cv2.destroyAllWindows()