import numpy
import cv2

burrito_path = input(".burrito image path: ")

with open(burrito_path, "r") as encoded:
    first_line = encoded.readline().strip()
    width, height = map(int, first_line.strip('&').split(','))

    image = numpy.zeros((height, width, 3), dtype=numpy.uint8)

    y = 0
    for line in encoded:
        line = line.strip(']\n')
        if line:
            pixels = line.split('|')
            for x in range(width):
                if pixels[x]:
                    b, g, r = map(int, pixels[x].split(','))
                    image[y, x] = [b, g, r]
            y += 1

cv2.imshow(burrito_path, image)
cv2.waitKey(0)
cv2.destroyAllWindows()