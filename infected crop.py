# Import necessary libraries
import cv2
import numpy as np

# Load the image of the cotton crop
img = cv2.imread('cotton.webp')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding to the image to create a binary image
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through each contour
for contour in contours:
    # Get the area of the contour
    area = cv2.contourArea(contour)
    
    # Calculate the perimeter of the contour
    perimeter = cv2.arcLength(contour, True)
    
    # Calculate the circularity of the contour
    circularity = 4 * np.pi * (area / (perimeter * perimeter))
    
    # If the circularity is less than a threshold value, the crop is infected
    if circularity < 0.7:
        print("Cotton crop is infected")
        break
    else:
        print("Cotton crop is healthy")