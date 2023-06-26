"""This module contains the functions to be used to add, remove or edit the metadata from a picture."""
from PIL import Image
from PIL.ExifTags import TAGS

# Open the image file
image = Image.open("image.jpg")

# Get the existing metadata
metadata = image.getexif()

# Add new metadata
metadata[TAGS["Software"]] = "My Image Editor"

# Save the modified image with the new metadata
image.save("new_image.jpg", exif=metadata)