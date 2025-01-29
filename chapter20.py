import cv2 as cv

# Load the video
cap = cv.VideoCapture(r"resources\1280x720_1mb.mp4")

if cap.isOpened():
    print('cap is ok')
else:
    print('cap is not ok')

frameNr = 0
skipFrame = 2 

while True:
    ret, frame = cap.read()  # Read a new frame within the loop
    if ret == False:
        print('no frame is read, if show in the end of the loop then ok')
        break

    if frameNr % skipFrame == 0:
        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg", frame)
        print(f"Saved frame_{frameNr}.jpg")
    frameNr += 1  # Increment frame number outside the if condition

cap.release()
