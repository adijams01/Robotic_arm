# import required libraries
import cvzone
import cv2
import serial
import time

# 2 seconds delay to start communication with arduino
time.sleep(2);

# video capture
cap=cv2.VideoCapture(1)

# calling hand detection function
detector=cvzone.HandDetector(maxHands=1,detectionCon=0.7)

# communication with arduino
mySerial=cvzone.SerialObject("COM7",9600,1)

location=""

while True:
    success,img=cap.read()
    img= detector.findHands(img)
    lmlist,bbox= detector.findPosition(img)
    fingers=[0,0,0,0,0]
    if lmlist:
        fingers=detector.fingersUp()

    try:

        # coordinates of midpoint
        x = bbox[0] + bbox[2] / 2
        y = bbox[1] + bbox[3] / 2

        # Left or right and Up or Down
        if (x <= 320):

            if (y <= 240):
                # location : A
                location = "1"
            else:
                # location : C
                location = "3"
        else:

            if (y <= 240):
                # location : B
                location = "2"
            else:
                # location : D
                location = "4"

        # Open or Close
        if (fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0):
            location+= "0"
        else:
            location+= "1"
        # hand sign to stop the code
        if(fingers[0]==0 and fingers[1]==1 and fingers[2]==0 and fingers[3]==0 and fingers[4]==1):
            location = "2"
            break

    except:
        pass
    print(location)

    # Send Data to arduino as a string
    mySerial.sendData(location)
    # Reset Data
    location=""

    cv2.imshow("Image",img)
    cv2.waitKey(1)
ser.close()