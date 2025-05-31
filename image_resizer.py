#!/usr/bin/env python3
# Note:
# Usage image_resizer.py image.jpg or png as argument
# The objective of this script is to resize any image to 500 x 500 for updating album art.

import os
import sys
from PIL import Image

def resize_image(image_path):
    # Check if the file exists
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        return

    # Check if the file has a supported extension
    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not image_path.lower().endswith(valid_extensions):
        print("Error: Unsupported file format. Please provide a JPEG or PNG image.")
        return

    try:
        # Open the image
        with Image.open(image_path) as img:
            # Resize the image to 500x500 pixels
            resized_img = img.resize((500, 500), Image.LANCZOS)

            # Prepare the output path
            dir_name = os.path.dirname(image_path)
            ext = os.path.splitext(image_path)[1].lower()
            output_filename = f"resized_image{ext}"
            output_path = os.path.join(dir_name, output_filename)

            # Save the resized image
            resized_img.save(output_path)
            print(f"Resized image saved as '{output_path}'.")

    except Exception as e:
        print(f"An error occurred while processing the image: {e}")

if __name__ == "__main__":
    # Check if the image path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
    else:
        image_path = sys.argv[1]
        resize_image(image_path)

