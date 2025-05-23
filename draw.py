import cv2 as cv
import numpy as np

# Blank Image
blank = np.zeros((500,500,3), dtype = 'uint8')  # Creating a Blank Image
blank[200:300, 300:400] = 0,0,255  # Changing Color
cv.imshow("Blank", blank)   # Showing Image

# Drawing Recatngle

# 2 pixel thick Border
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)

# Filled
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Drawing Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

#Drawing line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# Wirte Text on Image
cv.putText(blank,'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)