import os
import glob
from face_clustering import cluster_faces

def test_cluster_faces():
    # Define input and output paths for testing
    input_folder = "test_data/extracted_faces"
    output_folder = "test_data/clustered_faces"
    expected_clusters = 5

    # Run the face clustering function
    cluster_faces(input_folder, output_folder, n_clusters=expected_clusters)

    # Check if the correct number of cluster folders have been created
    cluster_folders = glob.glob(os.path.join(output_folder, "Cluster_*"))
    assert len(cluster_folders) == expected_clusters

    # Check if each cluster folder has at least one image
    for folder in cluster_folders:
        image_files = glob.glob(os.path.join(folder, "*.jpg"))
        assert len(image_files) > 0

    # Clean up the output folder (you can comment this out if you want to keep the clustered_faces for inspection)
    for folder in cluster_folders:
        image_files = glob.glob(os.path.join(folder, "*.jpg"))
        for file in image_files:
            os.remove(file)
        os.rmdir(folder)
