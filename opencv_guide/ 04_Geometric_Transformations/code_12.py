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
# Define new dimensions (width, height)
new_width = 500
new_height = 400

resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
                                    # images can be resized to specific fixed sizes
                                    # interpolation takes in argument INTER_CUBIC for high quality resolution
#-------------------------------------------------------------------------------
cv2.imshow('Image', img)

cv2.imshow('Image_resized', resized_img)
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------