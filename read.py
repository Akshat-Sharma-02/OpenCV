import cv2 as cv

# <----------- Image Capture --------------------->

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# cv.waitKey(0)


# <----------- Video Capture --------------------->

# path1 = 0   # For System Cam Feed
# path2 = 'Videos/Model_1.mp4'    # For Video in System
# capture = cv.VideoCapture(path2)

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()    