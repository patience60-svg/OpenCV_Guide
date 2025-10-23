#-------------------------------------------------------------------------------
#            save the live stream as a video file 
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
cap = cv2.VideoCapture(0)
#-------------------------------------------------------------------------------
# an image or video has pixels in a field
# this field size is given as width * height
# in which width is width of image or video frame &
# height is height of image or video frame
# for example; image size of 640 by 480 
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # get frame width of live stream from camera
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # get frame height of live stream from camera 
fps = 10 # set the frames per second(fps) a live stream should be saved with
#-------------------------------------------------------------------------------
vid_format = cv2.VideoWriter_fourcc(*'mp4v') # set Codec for .mp4 format

# set video saver with path a video should be saved to, together with video format, fps and field size
vid_save_as = cv2.VideoWriter('vids/Webcam_Feed.mp4', vid_format, fps, (frame_width, frame_height))
#-------------------------------------------------------------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    cv2.imshow('Webcam Feed', frame)

    vid_save_as.write(frame) # save live stream frame by frame

    if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
#-------------------------------------------------------------------------------
cap.release()
vid_save_as.release()  # collapes video saver
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------