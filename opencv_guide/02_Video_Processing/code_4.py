#-------------------------------------------------------------------------------
#            read and display(stream) a saved video file
#-------------------------------------------------------------------------------
import cv2 
import numpy as np # though not neccesary, it's good practice to import numpy
#-------------------------------------------------------------------------------
vid_path = 'vids/vid_1.mp4' # set video path
cap = cv2.VideoCapture(vid_path) # VideoCapture() load video
#-------------------------------------------------------------------------------
# set a loop by setting while() to true
# since VideoCapture load video frame by frame, or image by image
while True:
    ret, frame = cap.read() # read frames loaded by VideoCapture and pass them to frame
                            # ret, keep in check whether frame is availble in cap.read()
                            # if cap.read() has a frame, ret is True and if not ret is False

    if not ret:   # if ret is not True then break
        break  
    
    cv2.imshow('Video', frame) # display video frame by frame
    cv2.waitKey(20)   # waitKey() with 20 passed allows imshow() to display 20 frames per second
#-------------------------------------------------------------------------------
cap.release() # stops VideoCapture from loading video
cv2.destroyAllWindows() # collapse the window panel through which video in displayed 
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------