#-------------------------------------------------------------------------------
#            drawing a line image
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
start_point = (50, 50)
end_point = (300, 100)
cv2.line(img, start_point, end_point, (0, 255, 0), 2) # line() draws a line between 2 points in an image
                                                      # a point has (x, y) coordinates in an image
                                                      # line() takes in image as first argument,
                                                      # then a point to start drawing from, in our case; start_point
                                                      # point at which the line must stop is given after; end_point
                                                      # fourth argument is the color of the line,
                                                      # last argument is the thickness of the line.
#-------------------------------------------------------------------------------
cv2.imshow('Image', img)
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------