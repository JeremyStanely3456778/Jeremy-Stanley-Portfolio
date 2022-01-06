import random
import cv2
import numpy
import os

def add_noise(img):

        # Getting the dimensions of the image
        row, col = img.shape

        # Randomly pick some pixels in the
        # image for coloring them white
        # Pick a random number between 300 and 10000
        number_of_pixels = random.randint(300, 10000)
        for i in range(number_of_pixels):
            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to white
            img[y_coord][x_coord] = 255

        # Randomly pick some pixels in
        # the image for coloring them black
        # Pick a random number between 300 and 10000
        number_of_pixels = random.randint(300, 10000)
        for i in range(number_of_pixels):
            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to black
            img[y_coord][x_coord] = 0

        return img

def add_salt_pepper_noise(file_path):
    for filename in os.listdir(file_path):
        try:
            print(filename)
            f_img = file_path + "/" + filename
            print(f_img)
            img = cv2.imread(f_img, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(f_img, add_noise(img))
        except:
            continue
        finally:
            continue




# salt-and-pepper noise can
# be applied only to greyscale images
# Reading the color image in greyscale image

# Storing the image


file_path = "/Users/JeremyStanley/Desktop/test_directory"
add_salt_pepper_noise(file_path)
'''
img = cv2.imread(file_path,
                 cv2.IMREAD_GRAYSCALE)

# Storing the image
cv2.imwrite(file_path,
            add_noise(img))
'''

