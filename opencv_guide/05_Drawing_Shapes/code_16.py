#-------------------------------------------------------------------------------
#            drawing a rectangular shape on image
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
# Define image dimensions
height = 400
width = 600
#-------------------------------------------------------------------------------
img = np.zeros((height, width, 3), np.uint8)
#-------------------------------------------------------------------------------
start_point = (70, 100)
end_point = (300, 200)
cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2) # rectangle() is adaptable
                                                         # it can draw a rectangle or a squre depending on start and end point
                                                         # image is the first argument it takes.
                                                         # then starting point of the rectangle; start_point
                                                         # followed by the end point of the rectangle in the image; end_point
                                                         # color is the fourth argument,
                                                         # thickness id the last argument
#-------------------------------------------------------------------------------
cv2.imshow('Image', img)
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------