import numpy as np
import cv2
from matplotlib import pyplot as plt

def tohsv(b,g,r):
    col=np.uint8([[[b,g,r]]])
    hsv_val=cv2.cvtColor(col,cv2.COLOR_BGR2HSV)
    print hsv_val,col.shape

if __name__ == '__main__':
    cap=cv2.VideoCapture(0)

    # kernel2 = np.array([[0, 0, 0],
    #                     [0, 1, 0],
    #                     [0, 1, 0],
    #                     [0, 1, 0],
    #                     [0, 0, 0]], np.uint8)

    kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    kernel2=np.ones((5,5),np.uint8)


    tohsv(0,255,0)
    while(True):
        _,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower1,upper1=np.array([160,30,30]),np.array([200,255,255])
        lower2,upper2=np.array([85,26,12]), np.array([130, 255, 255])

        mask=cv2.inRange(hsv,lower1,upper1)
        # mask2=cv2.inRange(hsv,lower2,upper2)
        # mask=cv2.bitwise_or(mask1,mask2)
        res=cv2.bitwise_and(frame,frame,mask=mask)

        dst=cv2.filter2D(frame,-1,kernel2)
        blur=cv2.blur(res,(3,3))
        gauss=cv2.GaussianBlur(res,(3,3),5)
        bil=cv2.bilateralFilter(res,10,75,75)
        diff=cv2.subtract(gauss,bil)
        closing =cv2.morphologyEx(gauss,cv2.MORPH_CLOSE,kernel)
        opening=cv2.morphologyEx(closing,cv2.MORPH_OPEN,kernel)

        cv2.imshow('Gauss',gauss)
        cv2.imshow('Blur',blur)
        cv2.imshow('AVG',frame)
        # cv2.imshow('Bilateral',bil)
        # cv2.imshow('Gauss',closing)
        # cv2.imshow('Morphed',opening)

        key = cv2.waitKey(10)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
