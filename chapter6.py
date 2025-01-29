import cv2

# Create a video capture object
cap = cv2.VideoCapture("resources/1280x720_5mb.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No video available")
        break
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
