import os
import glob

# Import the function from face_clustering.py that you want to test
# For example, if the function is named 'cluster_faces'
from face_clustering import cluster_faces

def test_face_clustering_function():
    cluster_faces()  # Assumes the function takes no arguments

    # Check if the output directory is created
    assert os.path.isdir('clustered_faces'), "Output directory 'clustered_faces' does not exist."

    # Check if the cluster subdirectories are created
    for i in range(5):  # Assumes 5 clusters as in your script
        cluster_dir = f'clustered_faces/Cluster_{i}'
        assert os.path.isdir(cluster_dir), f"Cluster directory {cluster_dir} does not exist."

        # Check if each cluster subdirectory contains image files
        cluster_images = glob.glob(f'{cluster_dir}/*.jpg')
        assert len(cluster_images) > 0, f"No images found in {cluster_dir}"
        
    
    # # TO DO!!!!! Add code to clean up the faces collected by the test_extract_faces_from_video.py file and the images and folders created by this test
    # for file_name in os.listdir(save_folder):
    #     os.remove(os.path.join(save_folder, file_name))
    # os.rmdir(save_folder)
