# Video-Face-Extractor-and-Clusterer
Code that extracts the faces from a video every second and classifies them based on how similar they look.

- [ ] Create function that checks if a video has been clustered from a database 
- [ ] If the video has not been clustered, function downloads the videos extracts the face of every face in a photo and saves the photo of the face in this format
- [ ] Make the code save the face photo in the format (video title)_(timestamp)_(order in which face was captured).png example (Avatar_189_3)
- [ ] Make the code save the photos to an existing or if not avaibale a new folder with its name as the title of the video.
- [ ] Create code that loops through every second of a video file and does the functionality above.
- [ ] Create code that runs the above functionality in a serverless funciton and saves them to an S3 storage bucket.
- [ ] Create code that classifies a bunch of face photos with good accuracy (85% and above)
- [ ] Modify the code above to extract all the face photos from an S3 storage to a serverless function
- [ ] Make code that does classification on the photos extracted above.
