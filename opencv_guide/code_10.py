#-------------------------------------------------------------------------------
#            flipping image
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
img_path = 'images/img_2.jpg' # set image path
#-------------------------------------------------------------------------------
img = cv2.imread(img_path)
#-------------------------------------------------------------------------------
img_flip_H = cv2.flip(img, 1) # flip() change sides of pixels in an image
                              # flip() with 1 passed, flip image around y-axis("image height")

img_flip_V = cv2.flip(img, 0) # flip() with 0 passed, flip image around x-axis("image width")

img_flip_Both = cv2.flip(img, -1) #flip() with -1 passed, flip image around both y-axis and x-axis
                                  # if flip the image first in y-axis, 
                                  # then it flips the already y-axis flipped image in x-axis
                                  # making it a both flip
#-------------------------------------------------------------------------------
cv2.imshow('Image', img)

cv2.imshow('Image_flip_Horizontal', img_flip_H)

cv2.imshow('Image_flip_Vertical', img_flip_V)

cv2.imshow('Image_flip_Both', img_flip_Both)
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------