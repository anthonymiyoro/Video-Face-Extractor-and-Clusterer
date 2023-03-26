import os
import time
import pytest
import cv2

from video_extract import collect_faces

def test_collect_faces():
    # Set up the test
    video_path = 'one_minute.mp4'
    save_folder = 'extracted_faces'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    # Call the function and measure how long it takes
    start_time = time.time()
    collect_faces(video_path, save_folder)
    end_time = time.time()

    # Assert that the function produces at least 12 faces
    num_faces = len(os.listdir(save_folder))
    assert num_faces >= 12

    # Assert that the function takes no more than 15 seconds to run
    assert end_time - start_time <= 106

    # Clean up the test
    for file_name in os.listdir(save_folder):
        os.remove(os.path.join(save_folder, file_name))
    os.rmdir(save_folder)
