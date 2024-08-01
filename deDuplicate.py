"""
Author: Tom Simic
Date: 2024-08-01
Purpouse: Search for duplicate pictures
"""
# import needed modules
# set constants
# create class/def Duplicates

# needed modules:
import os
from PIL import Image
from sources.getMean import Mean

# constants
# augment later for user's selection
CHOSEN_PATH = r'C:\Users\totalyscrewedup\Pictures\deDuplicateTestPics'
FILE_TYPE = ('.png', '.jpg')  # augment later for user's selection

# Testing progress:
# curr_path = os.getcwd()
# print(curr_path)
# print(CHOSEN_PATH)

# creating Duplicates class


class Duplicates():
    _total = 0

    def find_dupes(dir):
        """Looks for duplicate mean values and compares them to individual pictures """
        temp = []
        for pic in (_ for _ in os.listdir(dir) if _.endswith(FILE_TYPE)):
            if not pic in temp:
                original = Image.open(os.path.join(dir, pic))
                original_mean = Mean(original).getMean()

                for comp_pic in (_ for _ in os.listdir(dir) if _.endswith(FILE_TYPE)):
                    if comp_pic != pic:
                        potential = Image.open(
                            os.path.join(dir, comp_pic))
                        potential_mean = Mean(potential).getMean()

                        if original_mean == potential_mean:
                            Duplicates._total += 1
                            yield pic, comp_pic

    def __str__(self) -> str:
        total = str(Duplicates._total)
        return total


# list files:
# for pic in (_ for _ in os.listdir(CHOSEN_PATH) if _.endswith((FILE_TYPE))):
#     print(pic)
if __name__ == "__main__":
    pic_path = Image.open(os.path.join(CHOSEN_PATH, 'profile_2.jpg'))
    # print(pic_path)
    pic = Mean(pic_path)
    # print(pic.getMean())
    folder = Duplicates.find_dupes(CHOSEN_PATH)
    for items in folder:
        print(f"The file {os.path.join(CHOSEN_PATH,
              items[0])} has following duplicates:")
        for item in items[1:]:
            print(os.path.join(CHOSEN_PATH, item))
            print("----")
        print("*" * 10)
    print(Duplicates._total)
