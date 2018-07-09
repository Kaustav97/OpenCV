import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    cap=cv2.VideoCapture(0)

    while(cap.isOpened()):
        _,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        lap=cv2.Laplacian(bw,cv2.CV_64F)
        edges=cv2.Canny(frame,100,200)

        # cv2.imshow('Laplacian',lap)
        # cv2.imshow('frame',hsv)
        cv2.imshow('BW',bw)
        cv2.imshow('Canny',edges)


        key=cv2.waitKey(25)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()