import numpy as np
from matplotlib import pyplot as plt
import cv2

if __name__ == '__main__':
    cap=cv2.VideoCapture(0)
    pic=cv2.imread('CR7.jpg',cv2.IMREAD_COLOR)
    pic=cv2.resize(pic,(600,600))
    ball=pic[364:545, 32:143, :]
    rsize,colsize=ball.shape[:2]
    b,g,r=cv2.split(ball)
    rball=cv2.merge([r,r,r])
    gball = cv2.merge([g, g, g])
    bball = cv2.merge([b,b,b])

    # cv2.imshow('org',ball)
    # cv2.imshow('rball', rball)
    # cv2.imshow('gball', gball)
    # cv2.imshow('bball', bball)
    # cv2.imshow('mask',mask)

    while(cap.isOpened()):
        ret,frame=cap.read()
        frame[32:32+rsize,32:32+colsize,:]=ball
        cv2.imshow('frame',frame)
        key=cv2.waitKey(25)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()