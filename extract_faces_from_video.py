import cv2
import os
import time

# Load the video file
# Replace video file with a video of your choice
video_file = "videos/Richardson.mp4"

# Create a directory to store extracted faces
output_folder = "extracted_faces"

def collect_faces(video_file, output_folder, frame_skip):
    cap = cv2.VideoCapture(video_file)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize variables
    frame_count = 0
    face_count = 0
    start_time = time.time()

    # Create the face cascade outside of the loop
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        # Read a frame
        ret, frame = cap.read()

        # Exit the loop if there are no more frames to read
        if not ret:
            break

        # Process only if frame_count is a multiple of (frame_skip + 1)
        if frame_count % (frame_skip + 1) == 0:
            # Extract faces from the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            # Save each face as an image in the output folder
            for (x, y, w, h) in faces:
                face = frame[y:y+h, x:x+w]
                cv2.imwrite(os.path.join(output_folder, "face_{:04d}.png".format(face_count)), face)
                face_count += 1

            # Display progress
            print("Processed frame {}".format(frame_count))

        # Increment the frame count
        frame_count += 1

    # Release the video capture object
    cap.release()

    # Display the time taken to process the video
    end_time = time.time()
    print("Time taken: {:.2f} seconds".format(end_time - start_time))

# Increase the frame_skip value to skip fewer frames (extract more faces)
collect_faces(video_file, output_folder, frame_skip=1)
