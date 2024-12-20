# Real-time Collision Avoidance Smart System for Dump Trucks using Deep Learning

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Inputs](#inputs)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to enhance safety in open-pit mining by dynamically adjusting the hazard zone around dump trucks based on vehicle speed and road conditions. The system utilizes **YOLO** for object detection, **segmentation** models for identifying road surfaces, and **Classifier** for analyzing weather conditions like rain or snow. This real-time solution provides visual alerts to enhance situational awareness and helps prevent accidents in the mining environment.

[Back to Top](#table-of-contents)

## Features
- **Dynamic Hazard Zone Adjustment**: The hazard zone automatically scales based on vehicle speed and road conditions.
- **Real-Time Road Segmentation and Road Condition Detection**: Integrates segmentation and classification to segment road surface and detect environmental conditions such as rain or snow.
- **Object Detection**: Uses YOLO to detect dump trucks, obstacles, and other objects in real time. (by Mr. Mohtashami)
- **Visual Feedback**: Provides immediate, real-time visual alerts with clear hazard zone indicators.

[Back to Top](#table-of-contents)

## Inputs
- **Camera Feed**: Real-time video input for detecting vehicles and road conditions.
- **Vehicle Speed Data**: Input data from speed sensors or camera-based tracking to determine vehicle velocity.
- **Weather Condition Data**: For weather detection including dry, wet, and snowy weather.

[Back to Top](#table-of-contents)

## Installation
To run the project locally, follow the steps below:

1. Clone this repository:
    ```bash
    https://github.com/Abyaneh/Real-time_Collision_Avoidance_System_for_Dump_Trucks
    ```
2. Change directory to the project folder:
    ```bash
    cd Real-time_Collision_Avoidance_System_for_Dump_Trucks
    
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

[Requirements](https://github.com/Abyaneh/Dynamic-Dump-Truck-Hazard-Zone-Detection-with-Road-Condition-Analysis/blob/main/requirements.txt)


[Back to Top](#table-of-contents)

## Usage
### Ground Zone Instruction Manual

#### Step 1: Setting up the Ground Zone Calibration
1. **Open the Project**: Start by opening the `Ground_Zone` folder.
2. **Access Calibration Code**: Open the `Ground_Zone_Calibration2.py` file. This section of the code is used to select the corner points of the yellow hazard zone. 
3. **Specify Camera or Video Input**: In the code, locate the line:  
   ```python
   camera_port = 'Data/output6.mp4'
4. Running the Calibration Code: After setting the video or camera input, run the code. The system will prompt you to select the four corner points of the yellow hazard zone in a clockwise direction, starting from the bottom-left corner. Use the mouse to click on each corner.
5. Save and View Selected Points: Once the corner points are selected, their coordinates are saved in the console output and in the file selected_points.txt located in the Weights folder.
#### Step 2: Running the Main Hazard Detection
1. Open the Main Code: After selecting the points, open the Main02.py file.
2. Specify Camera or Video Input: Similar to the calibration step, you can modify the camera_port to specify the input video or live camera feed.
3. Run the Code: Once the input is set, run the file. The system will display two hazard zones (yellow and red) and detect objects within the field of view using the YOLOv9t model. ( You can change yolov9t.pt to yolo11n.pt or any yolo version you want )
- When objects enter the yellow or red hazard zones, the color of their bounding box will change accordingly.
4. Exit and Save: Press q to stop the video and halt the code execution.
5. Save the Output Video: After the code runs, the resulting video will be automatically saved as output_video.mp4.
##### Running the Main Application
1. Run the main application:
python main.py
2. Real-time Detection: The system will process the camera feed, detecting both the vehicle’s speed and road conditions in real time.
3. Visual Output: The hazard zones (red and yellow) will dynamically adjust based on vehicle speed and road surface conditions (wet, snowy, etc.).
   
[Back to Top](#table-of-contents)

## Results
Testing results in various conditions:
- **Dry Road**: Standard hazard zone adjustment based on vehicle speed.
- **Wet/Snowy Conditions**: Expanded hazard zones to account for decreased control on slippery surfaces.
- **Real-Time Alerts**: Immediate visual cues when entering hazardous zones, enhancing operator awareness and reducing risk.

### Visual Examples
- **Hazard Zone in Dry Conditions:**

![Dry Conditions](https://github.com/Abyaneh/Dynamic-Dump-Truck-Hazard-Zone-Detection-with-Road-Condition-Analysis/blob/main/photos/output2.jpg)

<img src="https://github.com/Abyaneh/Dynamic-Dump-Truck-Hazard-Zone-Detection-with-Road-Condition-Analysis/blob/main/photos/output1.jpg" alt="Final_Assembled_Device" width="600"/>

![Dry Conditions](https://github.com/Abyaneh/Dynamic-Dump-Truck-Hazard-Zone-Detection-with-Road-Condition-Analysis/blob/main/photos/output3.jpg)


- **Expanded Hazard Zone in Wet/Snowy Conditions:**

    - Coming soon


- **Video output:**

    - [Watch the Demo Video](https://github.com/Abyaneh/Dynamic-Dump-Truck-Hazard-Zone-Detection-with-Road-Condition-Analysis/blob/main/video/output_video.mp4)

## Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add a new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request for review.

[Back to Top](#table-of-contents)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Abyaneh/Dynamic-Dump-Truck-Hazard-Zone-Detection-with-Road-Condition-Analysis/blob/main/LICENSE) file for details.

[Back to Top](#table-of-contents)
