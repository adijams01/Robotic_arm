# Gesture-Controlled Robotic Arm with Computer Vision
This repository contains code and instructions for building a robotic arm using OpenCV and Google's MediaPipe Library.

The project uses a webcam to track the movements of the user's hand using MediaPipe's Hand Tracking module, and uses this information to control the movements of the robotic arm. The robotic arm is controlled using an Arduino board and servo motors.

## Prerequisites
* Python 3.7.x (it only worked on version less than 3.8)
* Arduino IDE
* OpenCV
* MediaPipe
* SerialDevice
* cvzone
* using pycharm is advisable

## Installation
1. Clone this repository to your local machine.
```
git clone https://github.com/adijams01/Robotic_arm.git
```
2. Install the required Python libraries.
```
pip install opencv-python mediapipe pyserial
```
3. Upload the [Robot_Arm.ino](https://github.com/adijams01/Robotic_arm/blob/main/2x2%20Grid%20Robotic%20Arm/Robot_Arm.ino) sketch to your Arduino board.

4. Connect the servo motors to the Arduino board.

5. Set proper communication with arduino and python script by tweaking this part of the code.
```
mySerial=cvzone.SerialObject("COM7",9600,1)
```


6. Run the [LRnUDnOC.py](https://github.com/adijams01/Robotic_arm/blob/main/2x2%20Grid%20Robotic%20Arm/LRnUDnOC.py) script.

```
python robotic_arm_mediapipe.py
```
## Usage
Position your hand in front of the webcam.

The robotic arm will follow the movements of your hand.

To stop the program, make the the following sign (index finger open and pinky finger open).

## Explanation


## Contributing
Contributions are welcome! If you find any bugs or have any ideas for improvement, please submit an issue or pull request.




