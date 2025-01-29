import cv2

# Create a video capture object
cap = cv2.VideoCapture("resources/1280x720_5mb.mp4")

# Video ki properties hasil karein
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# VideoWriter object create karein
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('resources/output_video5mbGray.mp4', fourcc, fps, (width, height), isColor=False)

# Pehle video write karein
print("Video writing shuru...")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray_frame)

# Video writer ko release karein
out.release()
print("Video writing khatam.")

# Ab video ko display karein
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Video ko shuru se play karein
print("Video display shuru...")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray_frame)
    
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# Resources release karein
cap.release()
cv2.destroyAllWindows()
print("Program khatam.")
