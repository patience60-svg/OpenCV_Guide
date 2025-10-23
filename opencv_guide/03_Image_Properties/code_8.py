#-------------------------------------------------------------------------------
#            color spaces: Introduction 
#-------------------------------------------------------------------------------
import cv2
import numpy as np
#-------------------------------------------------------------------------------
img_path = 'images/img_2.jpg' # set image path
#-------------------------------------------------------------------------------
# images are made up of pixels
# most of the time each pixel contains color('s') channels in RGB
# RGB: Red, Green, and Blue which are fundamental colors for digital screen

# OpenCV by default has image color set in BGR
# BGR: Blue, Green, and Red.

img = cv2.imread(img_path) # load image, set in BGR by default

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to RGB

# both BGR and RBG have color channels in range 0-255 per channel on scale
# (255, 255, 255) or (0, 0, 0) or (255, 50, 100) or (0, 255, 0) to form a color

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV
                                               # HSV: Hue, Saturation, Value
                                               # it separates color(Hue) from intensity(Value)
                                               # or "how much of color A in an image?"

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts to grayscale
                                                 # GrayScale: a way to represent an images brightness
                                                 # without any color, ("black" and "white" images)

img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#-------------------------------------------------------------------------------
cv2.imshow('Image', img)

cv2.imshow('Image_RGB', img_rgb)

cv2.imshow('Image_HSV', img_hsv)

cv2.imshow('Image_Gray', img_gray)

cv2.imshow('Image_LAB', img_lab)
#-------------------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------