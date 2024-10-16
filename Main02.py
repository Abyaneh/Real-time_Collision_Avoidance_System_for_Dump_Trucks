import numpy as np
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from glob import glob
import random
import cv2
import warnings
from threading import Thread
import time
import winsound
warnings.simplefilter('ignore')
import ultralytics
from ultralytics import YOLO
# import Distance
from Ground_Zone import Ground_Zone as gz  

########Change these
camera_port ='Data/output6.mp4' #'Data/videos/test.mp4' #'
realtime = True#False
yolo_model = YOLO('Weights/yolov9t.pt')   
'''
You can change yolov9t.pt to yolo11n.pt or any yolo version you want 
Note: I uploaded five yolo versions, if you want another version, you need to download it first
'''

# Function to perform object detection on an image
def detect_objects(image):
    yolo_outputs = yolo_model.predict(image)
    output = yolo_outputs[0]
    box = output.boxes
    names = output.names
    detections = []
    for j in range(len(box)):
        labels = names[box.cls[j].item()]
        coordinates = box.xyxy[j].tolist()
        confidence = np.round(box.conf[j].item(), 2)
        detection = {
            'label': labels,
            'coordinates': coordinates,
            'confidence': confidence
        }
        detections.append(detection)
    return detections

# Function to read frames from webcam and perform object detection
def webcam_object_detection():
    cap = cv2.VideoCapture(camera_port)
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')                # taghir
    output_video = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))
    
    selected_points = gz.read_points_from_file('Weights/selected_points.txt')
    xs, ys = zip(*selected_points)# xs[0] = x1, xs[1] = x2, xs[2] = x3, xs[3] = x4 // ys[0] = y1, ys[1] = y2, ys[2] = y3, ys[3] = y4
    width_1 = xs[0] + xs[3] #for mean amount in the function of finding D1, D2
    
    i=0





    while True:
        ret, frame = cap.read()
        if not ret:
            break
        i=i+1
        if not (i % 7) == 0:
            continue

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        detections = detect_objects(image)
        
        for detection in detections:
            coordinates = detection['coordinates']
            labels = detection['label']            
            if len(coordinates) >= 4:  # Ensure there are enough coordinates
                x1, y1, x2, y2 = coordinates
                x_left = x1
                x_center = (x1+x2)/2
                y_center = (y1+y2)/2
                x_right = x2               
                bb_height = y2 - y1

                ## Code for GROUND_ZONE
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2) # green
                
                if y2 > ys[0]: #Red area
                    D1 = ( (x_left - xs[1]) * (ys[0] - ys[1]) ) - ( ( y2 - ys[1]) * (xs[0] - xs[1]) )   # for posetive slop
                    D2 = ( (x_left - xs[2]) * (ys[3] - ys[2]) ) - ( ( y2 - ys[2]) * (xs[3] - xs[2]) )   # for negative slop
                    D3 = ( (x_center - xs[1]) * (ys[0] - ys[1]) ) - ( ( y2 - ys[1]) * (xs[0] - xs[1]) )     
                    D4 = ( (x_center - xs[2]) * (ys[3] - ys[2]) ) - ( ( y2 - ys[2]) * (xs[3] - xs[2]) )
                    D5 = ( (x_right - xs[1]) * (ys[0] - ys[1]) ) - ( ( y2 - ys[1]) * (xs[0] - xs[1]) )        
                    D6 = ( (x_right - xs[2]) * (ys[3] - ys[2]) ) - ( ( y2 - ys[2]) * (xs[3] - xs[2]) )
                    # D1, D2 = alert_situation(x1, x2, y1, y2, width_1, xs=xs, ys=ys)
                    if (D1>0 and D2<0) or (D3>0 and D4<0) or (D5>0 and D6<0):
                        if (labels == 'person' or labels == 'car'):
                            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)                
                            print('In the red area')
                elif ys[0] > y2 > ys[1]:   # yellow area
                    D1 = ( (x_left - xs[1]) * (ys[0] - ys[1]) ) - ( ( y2 - ys[1]) * (xs[0] - xs[1]) )     
                    D2 = ( (x_left - xs[2]) * (ys[3] - ys[2]) ) - ( ( y2 - ys[2]) * (xs[3] - xs[2]) )     
                    D3 = ( (x_center - xs[1]) * (ys[0] - ys[1]) ) - ( ( y2 - ys[1]) * (xs[0] - xs[1]) )     
                    D4 = ( (x_center - xs[2]) * (ys[3] - ys[2]) ) - ( ( y2 - ys[2]) * (xs[3] - xs[2]) )
                    D5 = ( (x_right - xs[1]) * (ys[0] - ys[1]) ) - ( ( y2 - ys[1]) * (xs[0] - xs[1]) )        
                    D6 = ( (x_right - xs[2]) * (ys[3] - ys[2]) ) - ( ( y2 - ys[2]) * (xs[3] - xs[2]) )
                    # D1, D2 = alert_situation(x1, x2, y1, y2, width_1, xs=xs, ys=ys)
                    if (D1>0 and D2<0) or (D3>0 and D4<0) or (D5>0 and D6<0):
                        if labels == 'person':
                            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 2)
                            print('In the yellow area')


        ## Ground Zone Detection    
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # ground = gz.draw_lines(image, selected_points)
        ground = gz.highlight_territories(image, selected_points)       # new
        

        cv2.imshow('Real-time Object Detection', ground )
        
        output_video.write(ground)                    # taghir
        if realtime == False:
            key = cv2.waitKey(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
       
    output_video.release()
    cap.release()
    cv2.destroyAllWindows()


webcam_object_detection()
# Start the webcam object detection in a separate thread
# webcam_thread = Thread(target=webcam_object_detection)
# webcam_thread.start()

# # Main thread continues executing other tasks
# # You can add more code here if needed

# # Wait for the webcam thread to finish
# webcam_thread.join()
print('ok')


















