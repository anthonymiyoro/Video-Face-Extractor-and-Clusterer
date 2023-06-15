import os
import glob
import sys
from face_clustering import cluster_faces

# Import the function from face_clustering.py that you want to test
sys.path.append("../")

path = "../extracted_faces"

def test_face_clustering_function():
    folder_path = path  # Replace with the actual folder path containing face images
    cluster_faces(folder_path)

    # Check if the output directory is created
    assert os.path.isdir('clustered_faces'), "Output directory 'clustered_faces' does not exist."

    # Check if the cluster subdirectories are created
    for i in range(5):  # Assumes 5 clusters as in your script
        cluster_dir = f'clustered_faces/Cluster_{i}'
        assert os.path.isdir(cluster_dir), f"Cluster directory {cluster_dir} does not exist."

        # Check if each cluster subdirectory contains image files
        cluster_images = glob.glob(f'{cluster_dir}/*.jpg') + glob.glob(f'{cluster_dir}/*.png')
        assert len(cluster_images) > 0, f"No images found in {cluster_dir}"

    # Clean up the generated files and folders
    os.system('rm -rf clustered_faces')  # Remove the clustered_faces folder

# Run the test
test_face_clustering_function()
