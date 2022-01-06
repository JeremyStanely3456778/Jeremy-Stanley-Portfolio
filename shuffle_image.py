from glob import glob
from random import shuffle
import os
import os
import random
import sys


class shuffle_images():
    def shuffle_imgs(folder_path):
        music_files = []
        dir_name = folder_path
        new_dir_name = '/Users/JeremyStanley/Desktop/shuffled_data'
        for file_name in os.listdir(dir_name):
            music_files.append(file_name)
        # shuffle list
        random.shuffle(music_files)
        print(music_files)
        for item in music_files:
            print(os.path.join(new_dir_name, item))

if __name__ == "__main__":
    folder_path = "/Users/JeremyStanley/Desktop/test_directory"
    shuffle_images.shuffle_imgs(folder_path)