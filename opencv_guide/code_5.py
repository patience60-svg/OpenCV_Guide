#-------------------------------------------------------------------------------
#    read and display(stream) a live camera feed through a web cam
#                                                              /camera on your PC
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
cap = cv2.VideoCapture(0) # pass numbers; 0, 1,... and figure which one is your camera
#-------------------------------------------------------------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    cv2.imshow('Webcam Feed', frame)
    cv2.waitKey(1) # always keep waitKey() with 1 passed when reading live camera feed
#-------------------------------------------------------------------------------
cap.release()
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------