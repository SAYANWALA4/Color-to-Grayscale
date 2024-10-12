import numpy as np
import cv2
import re


def read_rgb_values(file_path):
    rgb_values = []
    with open(file_path, 'r') as file:
        for line in file:
            # to find RGB values in the line
            match = re.search(r"Pixel at \((\d+), (\d+)\): R=(\d+), G=(\d+), B=(\d+)", line)
            if match:
                x, y, r, g, b = map(int, match.groups())
                rgb_values.append((x, y, r, g, b))
    return rgb_values


def create_image_from_rgb(rgb_values, width, height):
    # Create an empty image
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Fill the image with the average RGB values
    for x, y, r, g, b in rgb_values:
        # Check if coordinates are within bounds
        if 0 <= x < width and 0 <= y < height:
            average_rgb = (r + g + b) // 3  # Calculate average
            img[y, x] = (average_rgb, average_rgb, average_rgb)  # Set pixel value

    return img


def main(width_user, height_user):
    # Path to the input file containing RGB values
    if width_user <= 0:
        width_user = 1920
        height_user = 1080
    
    elif height_user <= 0:
        width_user = 1920
        height_user = 1080
        
    input_file_path = 'Store_Values.txt'

    # Read the RGB values from the file
    rgb_values = read_rgb_values(input_file_path)

    # Determine the image dimensions (based on your previous data)
    # Make sure this matches the original image dimensions
    width = width_user  # Change to your image width
    height = height_user  # Change to your image height

    # Create the image from RGB values
    img = create_image_from_rgb(rgb_values, width, height)

    # Save the image
    output_image_path = 'output_image.png'
    cv2.imwrite(output_image_path, img)

    print(f"Image created and saved to {output_image_path}")
