# Video-Face-Extractor-and-Clusterer

Code that extracts the faces from a video every second and classifies them based on how similar they look.

## Documentation for Face Extraction from Video Code

### Overview

The provided code extracts faces from a given video file and saves each extracted face as a separate image file in a specified output folder. The code uses the OpenCV library to perform face detection and image processing.

### How to use the code

To use the code, first specify the path to the video file from which you want to extract faces. Then specify the name of the output folder where the extracted faces will be saved. Optionally, you can set the `frame_skip` parameter to control how frequently the frames from the video are processed. For example, if `frame_skip` is set to 5, every 6th frame will be processed, and the others will be skipped.

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






Run test collect.py to collect the faces from a video and save them to a folder.

To test this functionality, install pytest and OpenCv then run the following command in the terminal.

```bash
python3 -m pytest
```

- [x] Make the code save the face photo in the format [video title]_[timestamp]_[order in which face was captured].png example [Avatar]_[189]_[3].png
- [x] Make the code save the photos to an existing or if not avaibale a new folder with its name as the title of the video.
- [x] Create code that loops through every second of a video file and does the functionality above.
- [x] Create tests for the above functionality.

- [ ] Put test code in a tests folder and make sure already written tests still work.
- [x] Set up a CI/CD pipeline where code does not push to github until every test file in the tests folder passes.
- [ ] Make face extraction take less than n seconds to complete where n is the length of video in seconds. (A 1 minute video should take less than 1 minute to extract faces if possible.)

- [ ] Create code that clusters a bunch of face photos with good accuracy (85% and above).
- [ ] Make code that does clustering on the photos extracted above.
- [ ] Write tests for the above functionality.

- [ ] Add face classification functionality.
- [ ] Add tests and documentation for this.


- [ ] Create documentation for the code written so far.
- [ ] Choose an appropriate license for the project.

- [ ] Create function that checks if a video has been clustered from a database.
- [ ] If the video has not been clustered, function downloads the videos extracts the face of every face in a photo and saves the photo of the face in this format.

- [ ] Create code that runs the above functionality in a serverless funciton and saves them to an S3 storage bucket.
- [ ] Modify the code above to extract all the face photos from an S3 storage to a serverless function.

https://github.com/varun-suresh/Clustering
