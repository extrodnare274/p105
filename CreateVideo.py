import os
import cv2

# Set the path for the Images folder
path = 'C:/Users/madha/Downloads/Project105'

# Create a list variable named Images
images = []

# Use a for loop to check each file in the folder
for file in os.listdir(path):
    # Separate the name and extension from a file name
    name, extension = os.path.splitext(file)

    # Check if the extension of the file matches with the image extension
    if extension.lower() in ['.png', '.jpg', '.jpeg']:
        # Create a variable file_name by concatenating the path and file name
        file_name = os.path.join(path, file)

        # Print the file name to check
        print(file_name)

        # Add each file to the images list
        images.append(file_name)

# Create a variable count to store len(images)
count = len(images)

# Read the first image from the images list
frame = cv2.imread(images[0])

# Capture width, height & channels
width, height, channels = frame.shape

# Create a tuple variable size using width, height
size = (width, height)

# Print size to check the result
print(size)

# Create a variable out and assign it with cv2.VideoWriter()
video_name = 'Project.avi'
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
out = cv2.VideoWriter(video_name, fourcc, fps, size)

# Create a for loop to add images to a VideoWriter
for i in range(count):
    # Read each image
    img = cv2.imread(images[i])

    # Add the image to the video using out.write()
    out.write(img)

# Release the VideoWriter
out.release()

# Print a message to know the video is complete
print("Done")
