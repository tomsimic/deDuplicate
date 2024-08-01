"""
Author: Tom Simic
Date: 2024-08-01
Purpouse: Search for duplicate pictures
"""
# import needed modules

import os
# from PIL import Image, ImageStat


# Testing progress:
curr_path = os.getcwd()
# augment later for user's selection
CHOSEN_PATH = r'C:\Users\totalyscrewedup\Pictures\deDuplicateTestPics'
FILE_TYPE = ('.png', '.jpg')  # augment later for user's selection

# list files:
for pic in (_ for _ in os.listdir(CHOSEN_PATH) if _.endswith((FILE_TYPE))):
    print(pic)
# print(curr_path)
# print(CHOSEN_PATH)
