# Video Writing in OpenCV: Step-by-Step Guide
1. Import the OpenCV Library
   
English: Import the OpenCV library

Urdu: OpenCV library ko import karein

python
`import cv2`
1. Create VideoCapture Object
English: Create a VideoCapture object to read the input video
Urdu: Input video ko parhne ke liye VideoCapture object banayein
python
cap = cv2.VideoCapture("input_video.mp4")
1. Get Video Properties
English: Get the video properties (width, height, fps)
Urdu: Video ki properties (width, height, fps) hasil karein
python
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
1. Create VideoWriter Object
English: Create a VideoWriter object, specifying codec, output filename, fps, and frame size
Urdu: VideoWriter object banayein, jis mein codec, output file ka naam, fps, aur frame size specify karein
python
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))
1. Frame Processing Loop
English: Loop through each frame of the input video
Urdu: Input video ke har frame ke liye loop chalayein
python
while True:
    ret, frame = cap.read()
    if not ret:
        break
1. Write Frames
English: Write the frame to the output video
Urdu: Frame ko output video mein likhein
python
    out.write(frame)
1. Display Frames (Optional)
English: Display the frame (optional)
Urdu: Frame ko display karein (optional)
python
    cv2.imshow('Frame', frame)
1. Exit Condition
English: Break the loop if 'q' is pressed
Urdu: Agar 'q' dabaya jaye to loop se bahar niklen
python
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
1. Release Resources
English: Release all resources
Urdu: Tamam resources ko release karein
python
cap.release()
out.release()
cv2.destroyAllWindows()
Complete Code
python
import cv2

# Create VideoCapture object
cap = cv2.VideoCapture("input_video.mp4")

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

# Process video
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Write frame
    out.write(frame)
    
    # Display frame
    cv2.imshow('Frame', frame)
    
    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
