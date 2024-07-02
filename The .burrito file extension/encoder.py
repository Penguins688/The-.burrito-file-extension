import cv2 
import os

image_path = input("Image Path: ")
filename_without_extension = os.path.splitext(image_path)[0]

image = cv2.imread(image_path)
width = int(image.shape[1])
height = int(image.shape[0])

with open(f"{filename_without_extension}.burrito", "w") as encoded:
    encoded.write(f"&{width}, {height}&\n")
    for y in range(height):
        for x in range(width):
            pixel_value = image[y, x]
            b, g, r = pixel_value
            encoded.write(f"{b},{g},{r}|")
        encoded.write("]\n")
    encoded.close()