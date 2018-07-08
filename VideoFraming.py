import numpy as np
import cv2

def readVideo(R,C,L):

    capR = cv2.VideoCapture(R)
    capC = cv2.VideoCapture(C)
    capL = cv2.VideoCapture(L)

    while (capR.isOpened() and capC.isOpened() and capL.isOpened()):
        
        retR, frameR = capR.read()
        if cv2.waitKey(1) & 0xFF == ord('q') or retR is False:
            break
        retC, frameC = capC.read()
        if cv2.waitKey(1) & 0xFF == ord('q') or retC is False:
            break
        retL, frameL = capL.read()
        if cv2.waitKey(1) & 0xFF == ord('q') or retL is False:
            break
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('R', frameR)

        cv2.imshow('C', frameC)

        cv2.imshow('L', frameL)



    # cap.release()
    cv2.destroyAllWindows()




readVideo("Right.avi","middle.avi","left.avi")
# readVideo("middle.avi")
# readVideo("Right.avi")


