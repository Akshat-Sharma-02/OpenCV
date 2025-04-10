import cv2 as cv

# <------------ Rescaling ------------>
# For System Videos
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


# For Live Videos

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

# <----------- Video Capture --------------------->

path1 = 0   # For System Cam Feed
path2 = 'Videos/Model_1.mp4'    # For Video in System

capture = cv.VideoCapture(path2)

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    frameResized = rescaleFrame(frame)
    cv.imshow('Video Resized', frameResized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# <-------- Image Cpature -------------->
# # ORIGINAL IMAGE
# img = cv.imread('Photos/cat.jpg')
# cv.imshow("Orignal Image", img)

# # RESIZED IMAGE
# img_Resized = rescaleFrame(img)
# cv.imshow("Resized Image", img_Resized)

# cv.waitKey(0) 