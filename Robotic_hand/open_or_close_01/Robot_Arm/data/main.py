import cvzone
import cv2

cap=cv2.VideoCapture(1)
detector=cvzone.HandDetector(maxHands=1,detectionCon=0.7)
mySerial=cvzone.SerialObject("COM6",9600,1)
while True:
    success,img=cap.read()
    img= detector.findHands(img)
    lmlist,bbox= detector.findPosition(img)
    # try:
    #     x = bbox[0] + bbox[2] / 2
    #     y = bbox[1] + bbox[3] / 2
    #
    #     if (y <= 240):
    #         if(x <= 120):
    #             location="A"
    #         elif (x > 120 and x <= 240):
    #             location = "B"
    #         elif (x > 240 and x <= 320):
    #             location = "C"
    #         elif (x > 320 and x <= 480):
    #             location = "D"
    #
    #     if (y > 240 and y <= 320):
    #         if (x <= 120):
    #             location = "E"
    #         elif (x > 120 and x <= 240):
    #             location = "F"
    #         elif (x > 240 and x <= 320):
    #             location = "G"
    #         elif (x > 320 and x <= 480):
    #             location = "H"
    #
    #     if (y > 320 and y <= 480):
    #         if (x <= 120):
    #             location = "I"
    #         elif (x > 120 and x <= 240):
    #             location = "J"
    #         elif (x > 240 and x <= 320):
    #             location = "K"
    #         elif (x > 320 and x <= 480):
    #             location = "L"
    #
    #     if (y > 480 and y <= 640):
    #         if (x <= 120):
    #             location = "M"
    #         elif (x > 120 and x <= 240):
    #             location = "N"
    #         elif (x > 240 and x <= 320):
    #             location = "O"
    #         elif (x > 320 and x <= 480):
    #             location = "P"
    # except:
    #     pass
    if lmlist:
        fingers=detector.fingersUp()
        # print(fingers)

        mySerial.sendData(fingers)
    cv2.imshow("Image",img)
    cv2.waitKey(1)