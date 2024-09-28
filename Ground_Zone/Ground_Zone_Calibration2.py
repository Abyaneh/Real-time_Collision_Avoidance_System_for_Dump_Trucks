import cv2
import time

# Global variable
points = []
camera_port='Data/output6.mp4'  
video_file=camera_port 

#######
def get_video_height(video_file):
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Error: Could not open video file")
        return None

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    return height

# Mouse callback function
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))
            print(f"Point {len(points)} selected: ({x}, {y})")
        if len(points) == 4:
            cv2.destroyWindow('Select Points')

# Function to display the video and allow point selection
def choose_four_points(video_path):
    global points
    points = []  # Reset points
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return []

    while len(points) < 4:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from the video.")
            break

        clone = frame.copy()
        time.sleep(0.005)
        cv2.namedWindow('Select Points')
        cv2.setMouseCallback('Select Points', select_points)
        cv2.imshow('Select Points', clone)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return points
def save_points_to_file(points, file_path):
    with open(file_path, 'w') as file:
        for point in points:
            file.write(f"{point[0]},{point[1]}\n")
            
selected_points = choose_four_points(camera_port)
print("Selected points:", selected_points)

xs, ys = zip(*selected_points)# xs[0] = x1, xs[1] = x2, xs[2] = x3, xs[3] = x4 // ys[0] = y1, ys[1] = y2, ys[2] = y3, ys[3] = y4
# print("X-coordinates:", xs)
# print("Y-coordinates:", ys)

y1 = int((ys[0] + ys[3])/2)
y4=y1
y2 = int((ys[1] + ys[2])/2)
y3=y2

slope_1 =( (y2 - y1) / (xs[1]- xs[0]) )
slope_2 = ( (y4 - y3) / (xs[3]- xs[2]) )

b_1 = (y1 - (slope_1*xs[0]) )
b_2 = (y3 - (slope_2*xs[2]) )

height = get_video_height(video_file)

x6 = int((height - b_1)/slope_1)
x5 = int((height - b_2)/slope_2)

y6 = height
y5 = height

final_points = []
final_points.append((xs[0], y1))
final_points.append((xs[1], y2))
final_points.append((xs[2], y3))
final_points.append((xs[3], y4))
final_points.append((x5, y5))
final_points.append((x6, y6))

save_points_to_file(final_points, 'Weights/selected_points.txt')
