## Documentation for Face Extraction from Video Code


### Overview
The provided code extracts faces from a given video file and saves each extracted face as a separate image file in a specified output folder. The code uses the OpenCV library to perform face detection and image processing.


### Requirements

- Python 3
- OpenCV library (cv2)

All required libraries are available from the requirements.txt file

### How to use the code

To use the code, first specify the path to the video file from which you want to extract faces. Then specify the name of the output folder where the extracted faces will be saved. Optionally, you can set the `frame_skip` parameter to control how frequently the frames from the video are processed. For example, if `frame_skip` is set to 5, every 6th frame will be processed, and the others will be skipped.


### Testing

The script contains a test implemented using pytest. The test verifies whether the face extraction process can be completed within a specific time frame. The test passes a video to the `collect_faces` function and tracks the time taken to process the video for face extraction. The test ensures that the processing time is less than or equal to half the length of the video. If this condition is satisfied, the test passes; otherwise, it fails. To run the test, ensure that pytest is installed and use the following command in your terminal:

```bash
python3 -m pytest
```

Replace `your_test_file.py` with the name of the test file containing the pytest function.

### Instructions for Using the Script

1. Place the video file in the same directory as the script, or provide the full file path to the video.
2. Update the `video_file` and `output_folder` variables to match your desired input and output.
3. Optionally, adjust the value of `frame_skip` to change the frequency of frame processing.
4. Run the script to extract faces from the video.
5. Optionally, run the pytest to verify the face extraction process's efficiency.

Note: Please refer to the code file and test file for more details on the implementation and testing.


Run test collect.py to collect the faces from a video and save them to a folder.


### Code Description

1. **Importing Libraries**: The code starts by importing the necessary libraries: `cv2` (OpenCV), `os`, and `time`.

2. **Setting Video File and Output Folder**: The path to the video file (`video_file`) and the name of the output folder (`output_folder`) are specified. You should provide the path to the video file you want to process.

3. **Function Definition - `collect_faces`**: The `collect_faces` function performs the face extraction process. It takes three arguments:
   - `video_file`: The path to the video file to process.
   - `output_folder`: The name of the output folder to save the extracted faces.
   - `frame_skip`: An optional parameter to determine how many frames to skip before processing the next frame.

4. **Opening Video File**: A video capture object (`cap`) is created using OpenCV's `cv2.VideoCapture` method, which opens the video file.

5. **Creating Output Folder**: The code checks if the specified output folder exists. If not, it creates the folder using the `os.makedirs` method.

6. **Initializing Variables**: The `frame_count` variable is initialized to keep track of the number of frames processed, and `face_count` is initialized to keep track of the number of faces extracted. The `start_time` variable is initialized to record the start time of the face extraction process for performance measurement.

7. **Loading Haar Cascade for Face Detection**: The Haar cascade classifier for frontal face detection is loaded using OpenCV's `cv2.CascadeClassifier` method.

8. **Processing Video Frames**: The code enters a loop to process each frame of the video. Within the loop:
   - A frame is read from the video capture object.
   - If there are no more frames to read, the loop exits.
   - If the `frame_count` is a multiple of `(frame_skip + 1)`, the frame is processed; otherwise, it is skipped.
     - The frame is converted to grayscale.
     - The `detectMultiScale` method is used to detect faces in the frame.
     - Each detected face is saved as an image file in the output folder. The filenames are formatted as `face_XXXX.png`, where `XXXX` is the face count.
     - The `face_count` is incremented.
   - The `frame_count` is incremented.

9. **Releasing Video Capture Object**: The video capture object is released after all frames have been processed.

10. **Displaying Processing Time**: The code calculates the total time taken to process the video and displays it.

To run the code, simply call the `collect_faces` function with the appropriate arguments. For example:

```python
collect_faces(video_file="one_minute.mp4", output_folder="extracted_faces", frame_skip=5)
```

This will extract faces from the video file "one_minute.mp4" and save them in the "extracted_faces" folder, processing every 6th frame.
To run the code, simply call the `collect_faces` function with the appropriate arguments. For example:

```python
collect_faces(video_file="one_minute.mp4", output_folder="extracted_faces", frame_skip=5)
```

This will extract faces from the video file "one_minute.mp4" and save them in the "extracted_faces" folder, processing every 6th frame.