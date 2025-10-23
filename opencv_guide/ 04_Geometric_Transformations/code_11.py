#-------------------------------------------------------------------------------
#            resizing image
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
img_path = 'images/img_2.jpg' # set image path
#-------------------------------------------------------------------------------
img = cv2.imread(img_path)
#-------------------------------------------------------------------------------
h, w, c = img.shape # get height and width of the image

# opencv has resize() function for reducing or enlarging image size
# resize() takes in 3 parameters,
# resize(image, desired_dimentions, interpolation)
img_reduction = cv2.resize(img, (int(w/2), int(h/2)), interpolation=cv2.INTER_AREA) 
                                                      # when reducing  image size,
                                                      # interpolation has INTER_AREA as passed argument
                                                      # here image width(w) & height(h) are reduced by half
                                                      # then using int() the reduced size is passed as integer
                                                                                    
img_enlarging = cv2.resize(img, (int(w*2), int(h*2)), interpolation=cv2.INTER_LINEAR)
                                                      # when enlarging image size,
                                                      # interpolation has INTER_LINEAR as passed argument
                                                      # here image w & h are doubled i size
#-------------------------------------------------------------------------------
cv2.imshow('Image', img)

cv2.imshow('Image_Reducton', img_reduction)

cv2.imshow('Image_Enlarging', img_enlarging)
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------