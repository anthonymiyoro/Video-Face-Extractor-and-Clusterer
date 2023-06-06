import os
import cv2
import numpy as np
from sklearn.cluster import KMeans

# Folder path containing the extracted faces
folder_path = 'extracted_faces'

# Resize parameters
target_width = 128
target_height = 128

# Function to resize an image to the target size
def resize_image(image):
    return cv2.resize(image, (target_width, target_height))

# Function to load and resize the face images
def load_faces(folder_path):
    face_images = []
    image_paths = []
    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)
        image = cv2.imread(image_path)
        if image is not None:
            resized_image = resize_image(image)
            face_images.append(resized_image)
            image_paths.append(image_path)
    return face_images, image_paths

# Create a folder for the clustered faces
output_folder = 'clustered_faces'
os.makedirs(output_folder, exist_ok=True)

# Load and resize the face images
face_images, image_paths = load_faces(folder_path)

# Convert the face images to a numpy array
face_images = np.array(face_images)

# Flatten the face images
num_samples, height, width, channels = face_images.shape
face_images_flat = face_images.reshape(num_samples, -1)

# Perform clustering using K-means
n_clusters = 5  # Number of desired clusters
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(face_images_flat)

# Get the cluster labels
labels = kmeans.labels_

# Create subfolders for each cluster
cluster_subfolders = [os.path.join(output_folder, f"Cluster_{i}") for i in range(n_clusters)]
for subfolder in cluster_subfolders:
    os.makedirs(subfolder, exist_ok=True)

# Save the faces in their respective cluster folders
for i, image_path in enumerate(image_paths):
    cluster_label = labels[i]
    image_name = os.path.basename(image_path)
    output_path = os.path.join(cluster_subfolders[cluster_label], image_name)
    cv2.imwrite(output_path, face_images[i])

    print(f"Saved {image_name} to Cluster {cluster_label}")
