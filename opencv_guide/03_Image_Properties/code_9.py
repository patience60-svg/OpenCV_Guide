#-------------------------------------------------------------------------------
#            getting shape of an image
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
img_path = 'images/img_2.jpg' # set image path
#-------------------------------------------------------------------------------
img = cv2.imread(img_path)
#-------------------------------------------------------------------------------
h, w, c = img.shape # for BGR & RGB, it gives image shape in height by width by color channels
                    # 'h' is height, 'w' is width, and 'c' is number of color channels image has.
                    
print(f'image_height: {h}, image_width: {w}, image_channels: {c}') # print image shape values

cv2.imshow('Image', img) 
# try different images to check there shapes
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------