# OpenCV_Guide:  OpenCV Image Processing Tutorial

A collection of Python scripts demonstrating basic image processing operations using OpenCV. These examples cover image loading, grayscale conversion, and image saving.

## Table of Contents
  - [Installation](#Installation)
  - [Reading & displaying image file](Reading & displaying image file)
  - [Converting color of image]
  - [Saving image file]

## 📁 Project Structure

opencv_guide/
├── images/
│ ├── img_1.jpg
├── code_1.py
├── code_2.py
├── code_3.py
└── README.md

### Installation

pip install opencv-python

## Reading & displaying image file

import cv2
img_path = 'images/img_1.jpg'
img = cv2.imread(img_path)
cv2.imshow('Image', img)
cv2.waitKey(0)
