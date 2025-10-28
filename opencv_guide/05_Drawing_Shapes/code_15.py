#-------------------------------------------------------------------------------
#            drawing a circular shape image
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
center = (300, 100)
radius = 80
cv2.circle(img, center, radius, (0, 0, 255), 1) # circle() draws a circle in an image
                                                # it takes in image as first argument; img
                                                # center of the circle on the image is second argument,
                                                # radius of the circle is third argument, 
                                                # color of the circle is fourth argument
                                                # thickness of the circle is last argument

#cv2.circle(img, center, radius, (0, 0, 255), -1) # uncomment this to see a filled circle
                                                  # that's after running the code with the first circle above  
#-------------------------------------------------------------------------------
cv2.imshow('Image', img)
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------