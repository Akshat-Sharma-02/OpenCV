import cv2 as cv
import numpy as np

img = cv.imread('Photos/PotHole_1.jpg')
# cv.imshow('PotHole', img)
resized = cv.resize(img, (800,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized_PotHole', resized)

blank = np.zeros(resized.shape[:2], dtype="uint8")

b,g,r = cv.split(resized)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(resized.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("Mereged", merged)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)


cv.waitKey(0)