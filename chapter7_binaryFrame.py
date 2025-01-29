import cv2

# Create a video capture object
cap = cv2.VideoCapture("resources/1280x720_5mb.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No video available")
        break
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    (thresh,binary)=cv2.threshold(gray_frame,100,200,cv2.THRESH_BINARY)
#to show in player
    cv2.imshow('binary', binary)
    cv2.imshow('gray frame',gray_frame)
    cv2.imshow('orignal',frame)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()