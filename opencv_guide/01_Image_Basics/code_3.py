#import opencv using cv2
import cv2

img_path = 'images/img_1.jpg' # set image path 

img = cv2.imread(img_path) # load image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # cvtColor() converts color of image to gray
                                                 # opencv reads image color in 'bgr' not 'rgb'
                                                 # 'bgr' : Blue, Green, Red
                                                 # image is converted from BGR to GRAY, 'COLOR_BGR2GRAY

cv2.imshow('Image', img_gray)   # display image
                                # change from img to img_gray

img_save_as = 'images/img_gray_1.jpg' # set path where image should be saved

cv2.imwrite(img_save_as, img_gray) # imwrite() saves image given to the path given
                                   # first variable is path image should be saved to, 
                                   # second image to be saved

cv2.waitKey(0) # end image display when any key is placed