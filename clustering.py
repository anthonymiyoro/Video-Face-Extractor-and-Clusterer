import os
import face_recognition
from sklearn.cluster import DBSCAN
import numpy as np

faces_folder = "extracted_faces"

def cluster_faces(input_folder_path, output_folder_path):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    # Load all face encodings
    face_encodings = []
    for filename in os.listdir(input_folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            image = face_recognition.load_image_file(os.path.join(input_folder_path, filename))
            face_encoding = face_recognition.face_encodings(image)
            if len(face_encoding) > 0:
                face_encodings.append(face_encoding[0])

    # Cluster the face encodings using DBSCAN
    X = np.array(face_encodings)
    clustering = DBSCAN(metric='euclidean', eps=0.5, min_samples=2).fit(X)

    # Create a dictionary to hold the cluster index for each face
    face_clusters = {}
    for i in range(len(clustering.labels_)):
        cluster_index = clustering.labels_[i]
        if cluster_index != -1:
            filename = os.listdir(input_folder_path)[i]
            if cluster_index not in face_clusters:
                face_clusters[cluster_index] = []
            face_clusters[cluster_index].append(filename)

    # Save the clustered faces in separate folders
    for cluster_index, filenames in face_clusters.items():
        cluster_folder = os.path.join(output_folder_path, f'cluster_{cluster_index}')
        os.makedirs(cluster_folder, exist_ok=True)
        for filename in filenames:
            src_path = os.path.join(input_folder_path, filename)
            dst_path = os.path.join(cluster_folder, filename)
            os.rename(src_path, dst_path)


cluster_faces(faces_folder, "clustered_faces")
