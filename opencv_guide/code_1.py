#import opencv using cv2
import cv2

img_path = 'images/img_1.jpg' # set image path

img = cv2.imread(img_path) # imread() load image given

cv2.imshow('Image', img)   # imshow() display loaded image

cv2.waitKey(0) # waitKey() with 0 passed end image display when any key is placed