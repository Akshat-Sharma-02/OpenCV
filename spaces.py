import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)


# BGR to GrayScale
grayScale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale", grayScale)


# BGR to HSV(Hue-Saturation-Value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)


# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB", lab)


rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)