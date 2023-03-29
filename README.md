# Video-Face-Extractor-and-Clusterer
Code that extracts the faces from a video every second and classifies them based on how similar they look.

- [x] Make the code save the face photo in the format [video title]_[timestamp]_[order in which face was captured].png example [Avatar]_[189]_[3].png
- [x] Make the code save the photos to an existing or if not avaibale a new folder with its name as the title of the video.
- [x] Create code that loops through every second of a video file and does the functionality above.
- [x] Create tests for the above functionality.

- [ ] Put test code in a tests folder and make sure already written tests still work.
- [ ] Set up a CI/CD pipeline where code does not push to github until every test file in the tests folder passes.
- [ ] Make face extraction take less than n seconds to complete where n is the length of video in seconds. (A 1 minute video should take less than 1 minute to extract faces if possible.)

- [ ] Create code that clusters a bunch of face photos with good accuracy (85% and above).
- [ ] Make code that does classification on the photos extracted above.
- [ ] Write tests for the above functionality.

- [ ] Create documentation for the code written so far.
- [ ] Choose an appropriate license for the project.

- [ ] Create function that checks if a video has been clustered from a database.
- [ ] If the video has not been clustered, function downloads the videos extracts the face of every face in a photo and saves the photo of the face in this format.

- [ ] Create code that runs the above functionality in a serverless funciton and saves them to an S3 storage bucket.
- [ ] Modify the code above to extract all the face photos from an S3 storage to a serverless function.

- [ ] Add face classification functionality.
- [ ] Add tests and documentation for this.


https://github.com/varun-suresh/Clustering
