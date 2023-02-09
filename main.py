import cv2
import cvzone
import time
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False




while True:
    imgBg = cv2.imread("Resources/BG.png")
    success, img = cap.read();
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]
    # find hands
    hands, img = detector.findHands(imgScaled)

    if startGame:

        if stateResult is False:
            # timer = time.time - initialTime
            # cv2.putText(imgBg.str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            # if timer > 3:
            #     stateResult = True
            #     timer = 0
                if hands :
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    print(fingers)

    imgBg[234:654,795:1195] = imgScaled



    # cv2.imshow("Image", img)
    cv2.imshow("BG", imgBg)
    # cv2.imshow("Scaled", imgScaled)
    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        # initialTime = time.time()