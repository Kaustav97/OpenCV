import numpy as np
import cv2
from matplotlib import pyplot as plt


if __name__ == '__main__':
    logo=cv2.imread('python.png',cv2.IMREAD_COLOR)
    pic=cv2.imread('CR7.jpg',cv2.IMREAD_COLOR)
    pic=cv2.resize(pic,(800,600),interpolation=cv2.INTER_CUBIC)
    rows,cols=logo.shape[:2]
    roi=pic[100:100+rows,100:100+cols,:]
    
    bwlogo=cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
    ret,mask=cv2.threshold(bwlogo,0,255,cv2.THRESH_BINARY_INV)
    mask=cv2.add(mask,bwlogo)
    # cv2.imshow('maskprev', mask)
    ret,mask=cv2.threshold(mask,254,255,cv2.THRESH_TOZERO)
    # mask=cv2.bitwise_not(mask)
    
    roi=cv2.bitwise_and(roi,roi,mask=mask)
    roi=cv2.add(roi,logo)

    pic[100:100 + rows, 100:100 + cols, :]=roi
    pic[300:400,:,:2]=pic[300:400,:,:2]*0.2
    pic[:300,:,1]=0
    pic[400:, :, 2]=pic[400:,:,2]*0.1
    # cv2.imshow('logo',logo)
    # cv2.imshow('pic', pic)
    # cv2.imshow('mask',mask)
    cv2.imshow('reds',pic)
    key=cv2.waitKey(0)
    if key==27:
        cv2.destroyAllWindows()
