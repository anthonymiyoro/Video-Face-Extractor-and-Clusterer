# Import the necessary libraries
import cv2
import os
import time

# Function to collect faces from a video
def collect_faces(video_file, output_folder, frame_skip=5):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video file
    video_capture = cv2.VideoCapture(video_file)

    # Load a pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Get the frames per second of the video
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Get the title of the video (excluding file extension)
    video_title = os.path.splitext(os.path.basename(video_file))[0]

    # Initialize variables to keep track of the frame number and face count
    frame_number = 0
    face_count = 0

    # Variable to store the second of video
    current_second = -1

    # Loop through each frame in the video
    while True:
        # Read the next frame
        ret, frame = video_capture.read()
        
        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # Increment the frame number
        frame_number += 1

        # Skip frames for faster processing
        if frame_number % frame_skip != 0:
            continue

        # Detect faces in the frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Calculate the second of video
        second = int(frame_number / fps)

        # Update face count if we are in a new second of video
        if current_second != second:
            current_second = second
            face_count = 0

        # Save the faces to the output folder
        for (x, y, w, h) in faces:
            face_count += 1
            face_image = frame[y:y+h, x:x+w]

            # Save the face using the specified naming format
            face_filename = f"{video_title}_{second}_{face_count}.jpg"
            face_filepath = os.path.join(output_folder, face_filename)
            cv2.imwrite(face_filepath, face_image)

    # Release the video capture object
    video_capture.release()

# Define the path to the video file and output folder
# Note: Please update the paths accordingly before running the code
video_file = "videos/one_minute.mp4"
output_folder = "extracted_faces"

# Uncomment the line below to collect faces from the video
# collect_faces(video_file, output_folder, frame_skip=5) # Note: If you want to skip more or fewer frames, you can specify the frame_skip parameter

