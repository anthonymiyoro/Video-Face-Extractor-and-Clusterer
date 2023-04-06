import cv2
import os
import time


# Load the video file
# Replace video file with a video of your choice
video_file = "one_minute.mp4"

# Create a directory to store extracted faces
output_folder = "extracted_faces"

def collect_faces(video_file, output_folder):
    cap = cv2.VideoCapture(video_file)


    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize variables
    frame_count = 0
    face_count = 0
    start_time = time.time()
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Loop through each second of the video
    while True:
        # Read the next second of frames
        frames = []
        for i in range(int(fps)):
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        # Exit the loop if there are no more frames to read
        if not frames:
            break

        # Extract faces from each frame in the second
        for frame in frames:
            # Extract faces from the frame
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            # Save each face as an image in the output folder
            for (x, y, w, h) in faces:
                face = frame[y:y+h, x:x+w]
                cv2.imwrite(os.path.join(output_folder, "face_{:04d}.png".format(face_count)), face)
                face_count += 1

        # Increment the frame count
        frame_count += int(fps)

        # Display progress
        print("Processed {} seconds of video".format(frame_count // fps))

    # Release the video capture object
    cap.release()

    # Display the time taken to process the video
    end_time = time.time()
    print("Time taken: {:.2f} seconds".format(end_time - start_time))

collect_faces(video_file, output_folder)
