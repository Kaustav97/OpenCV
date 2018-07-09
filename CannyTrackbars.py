import numpy as np
import cv2

def nothing(x):
    pass

if __name__ == '__main__':
    cap=cv2.VideoCapture(0)
    window='Canny'

    # MUST create a named window for trackbars!
    #OR add below another image
    cv2.namedWindow(window)

    cv2.createTrackbar('first',window, 0, 255, nothing)
    cv2.createTrackbar('second',window, 0, 255, nothing)

    while(cap.isOpened()):
        _,frame=cap.read()

        fst=cv2.getTrackbarPos('first',window)
        sec=cv2.getTrackbarPos('second',window)

        canny=cv2.Canny(frame,fst,sec)
        kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
        canny2=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
        # canny2=cv2.erode(canny2,kernel,iterations=5)

        cv2.imshow('original',canny)
        cv2.imshow('morph',canny2)

        cv2.imshow(window,np.zeros((10,600,3),np.uint8))
        key=cv2.waitKey(25)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()