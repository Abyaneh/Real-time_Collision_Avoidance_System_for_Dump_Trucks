import cv2
import numpy as np

def draw_lines(image, points):
    if len(points) >= 4:
    # Draw line from point 1 to point 2
        cv2.line(image, points[0], points[1], (0, 255, 255), 2)            # yellow
         # Extend the line from point 1 to point 2 vertically to the specified height
        x1, y1 = points[0]
        x2, y2 = points[1]
        if y2 != y1:
            slope = (x2 - x1) / (y2 - y1)
            #x_extended_1 = int(x2 + slope * (height - y2))
            #cv2.line(image, points[0], (x_extended_1, height), (0, 0, 255), 2)          
        # Draw line from point 3 to point 4
        cv2.line(image, points[2], points[3], (0, 255, 255), 2)           # yellow
        # Extend the line from point 3 to point 4 vertically to the specified height
        x3, y3 = points[2]
        x4, y4 = points[3]
        x5, y5 = points[4]
        x6, y6 = points[5]
        if y4 != y3:
            # slope = (x4 - x3) / (y4 - y3)
            #x_extended_2 = int(x4 + slope * (height - y4))
            #cv2.line(image, points[3], (x_extended_2, height), (0, 0, 255), 2)
            #cv2.line(image, (x_extended_1, height), (x_extended_2, height), (0, 0, 255), 2)            
            cv2.line(image, points[1], points[2], (0, 255, 255), 2)      # yellow
            cv2.line(image, points[0], points[3], (0, 255, 255), 2)      # yellow
            cv2.line(image, points[3], points[4], (0, 0, 255), 2)
            cv2.line(image, points[4], points[5], (0, 0, 255), 2) 
            cv2.line(image, points[5], points[0], (0, 0, 255), 2)           
        
    return image


# Function to highlight territories between specified points
# def highlight_territories(image, points):
#     if len(points) >= 6:
#         # Draw a polygon to highlight territory between points 1, 2, 3, 4 (red)
#         pts_red = [points[0], points[1], points[3], points[2]]
#         cv2.fillPoly(image, [pts_red], (0, 0, 255))
        
#         # Draw a polygon to highlight territory between points 2, 3, 5, 6 (yellow)
#         pts_yellow = [points[1], points[4], points[5], points[2]]
#         cv2.fillPoly(image, [pts_yellow], (0, 255, 255))
        
    # return image

def read_points_from_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = line.strip().split(',')
            points.append((int(x), int(y)))
    return points

def highlight_territories(image, points):
    if len(points) >= 6:
        # Draw a polygon to highlight the upper territory (yellow)
        pts_yellow = [points[0], points[1], points[2], points[3]]
        overlay = image.copy()
        cv2.fillPoly(overlay, [np.array(pts_yellow)], (0, 255, 255))  # Yellow
        cv2.addWeighted(overlay, 0.3, image, 0.7, 0, image)

        # Draw a polygon to highlight the lower territory (red)
        pts_red = [points[0], points[3], points[4], points[5]]
        overlay = image.copy()
        cv2.fillPoly(overlay, [np.array(pts_red)], (0, 0, 255))  # Red
        cv2.addWeighted(overlay, 0.3, image, 0.7, 0, image)
        
    return image