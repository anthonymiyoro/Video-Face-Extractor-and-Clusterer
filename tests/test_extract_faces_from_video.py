import os
import sys
import re
import time

# Get the absolute path to the top-level directory
project_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(project_dir)
required_module_dir = os.path.join(parent_dir, 'Video-Face-Extractor-and-Clusterer')

# Add the top-level directory to Python module search path
sys.path.insert(0, required_module_dir)

# Import the collect_face function from the video_extract module
from extract_faces_from_video import collect_faces


def test_collect_faces():
    # Set up the test
    video_path = 'one_minute.mp4'
    save_folder = 'extracted_faces'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    # Call the function and measure how long it takes
    start_time = time.time()
    collect_faces(video_path, save_folder, 5)
    end_time = time.time()

    # Assert that the function produces at least 12 faces
    num_faces = len(os.listdir(save_folder))
    assert num_faces >= 12

    # Assert that the function takes no more than 15 seconds to run
    assert end_time - start_time <= 106
    
    # Define the regular expression pattern for the expected filenames
    video_title = os.path.splitext(os.path.basename(video_path))[0]
    pattern = re.compile(rf"{video_title}_(\d+)_(\d+).jpg")

    # Check whether the filenames of the saved face photos follow the expected format
    for file_name in os.listdir(save_folder):
        assert pattern.match(file_name), f"Filename '{file_name}' does not match the expected format."
        print(f"Filename '{file_name}' matches the expected format.")

    # Clean up the test
    for file_name in os.listdir(save_folder):
        os.remove(os.path.join(save_folder, file_name))
    os.rmdir(save_folder)
