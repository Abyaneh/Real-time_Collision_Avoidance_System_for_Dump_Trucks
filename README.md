# Dynamic Dump Truck Hazard Zone Detection with Road Condition Analysis

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
This project aims to enhance safety in open-pit mining by dynamically adjusting the hazard zone around dump trucks based on vehicle speed and road conditions. The system utilizes **YOLO** for object detection, **segmentation** models for identifying road surfaces, and **Transformers** for analyzing weather conditions like rain or snow. This real-time solution provides visual alerts, optimizing safety by scaling the hazard zone according to both road and speed conditions.

[Back to Top](#table-of-contents)

## Features
- **Dynamic Hazard Zone Adjustment**: The hazard zone automatically scales based on vehicle speed and road conditions.
- **Real-Time Road Condition Detection**: Integrates segmentation and Transformers to detect environmental conditions such as rain or snow.
- **Object Detection**: Uses YOLO to detect dump trucks, obstacles, and other objects in real time.
- **Visual Feedback**: Provides immediate, real-time visual alerts with clear hazard zone indicators.
- **Scalable for Industrial Use**: Tailored for large-scale environments like open-pit mines, with real-time adaptability.

[Back to Top](#table-of-contents)

## Inputs
- **Camera Feed**: Real-time video input for detecting vehicles and road conditions.
- **Vehicle Speed Data**: Input data from speed sensors or camera-based tracking for determining vehicle velocity.
- **Weather Condition Data**: Road surface detection using segmentation and Transformer models.

[Back to Top](#table-of-contents)

## Installation
To run the project locally, follow the steps below:

1. Clone this repository:
    ```bash
    git clone https://github.com/Abyaneh/dump-truck-hazard-zone.git
    ```
2. Change directory to the project folder:
    ```bash
    cd dump-truck-hazard-zone
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

[Back to Top](#table-of-contents)

## Usage
1. **Run the main application**:
    ```bash
    python main.py
    ```
2. **Real-time Detection**: The system will process the camera feed, detecting both the vehicle’s speed and road conditions in real time.
3. **Visual Output**: The hazard zones (red and yellow) will dynamically adjust based on vehicle speed and road surface conditions (wet, snowy, etc.).

[Back to Top](#table-of-contents)

## Results
Testing results in various conditions:
- **Dry Road**: Standard hazard zone adjustment based on vehicle speed.
- **Wet/Snowy Conditions**: Expanded hazard zones to account for decreased control on slippery surfaces.
- **Real-Time Alerts**: Immediate visual cues when entering hazardous zones, enhancing operator awareness and reducing risk.

### Visual Examples
- **Dynamic Hazard Zone in Dry Conditions:**
    ![Dry Conditions](https://github.com/Abyaneh/Dynamic-Dump-Truck-Hazard-Zone-Detection-with-Road-Condition-Analysis/blob/main/output1.jpg)
- **Expanded Hazard Zone in Wet Conditions:**
    ![Wet Conditions](./images/wet_conditions.png)
  
[Watch the Demo Video](./videos/demo.mp4)

[Back to Top](#table-of-contents)

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
