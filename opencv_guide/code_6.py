#-------------------------------------------------------------------------------
#            add a breaker to your program
#            that allows you to terminate your program when is running
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
cap = cv2.VideoCapture(0)
#-------------------------------------------------------------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): # add a keyboard key to terminate the code when placed
                    break                 # when 'q' on keyboard is places, code is terminated
#-------------------------------------------------------------------------------
cap.release()
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------