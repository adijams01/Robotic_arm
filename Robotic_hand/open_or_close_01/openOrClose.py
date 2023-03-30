import cvzone
import cv2

import serial
import time

# ser = serial.Serial("COM6", 9600)  # open serial connection
time.sleep(2);

cap=cv2.VideoCapture(1)
detector=cvzone.HandDetector(maxHands=1,detectionCon=0.7)
mySerial=cvzone.SerialObject("COM6",9600,1)
location=""
while True:
    success,img=cap.read()
    img= detector.findHands(img)
    lmlist,bbox= detector.findPosition(img)
    fingers=[0,0,0,0,0]
    if lmlist:
        fingers=detector.fingersUp()
    if(fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0):
            # ser.write(b'0')
            location = "0"
            l=0
            # ser.write(b'0')
    elif(fingers[0]==0 and fingers[1]==1 and fingers[2]==0 and fingers[3]==0 and fingers[4]==1):
        location = "2"
        break
    else:
            location="1"
            l=1
            # ser.write(b'1')
    print(location)
    # ser.write(l)
        # try:
    mySerial.sendData(location)
        # except:
        #     pass
    cv2.imshow("Image",img)
    cv2.waitKey(1)
ser.close()