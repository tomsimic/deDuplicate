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
from get_mean import Picture

# augment later for user's selection
# constants for testing needs
CHOSEN_PATH = r'C:\Users\totalyscrewedup\Pictures\deDuplicateTestPics'
FILE_TYPE = ('.png', '.jpg')  # augment later for user's selection


# creating Duplicates class

def find_dupes(root=os.getcwd(), ft=FILE_TYPE):
    """Looks for duplicate mean values and compares them to individual pictures, to return iterable of tuples """
    temp = {}
    for pic in (_ for _ in os.listdir(root) if _.endswith(ft)):
        orig_path = Picture(root, pic)
        orig_mean = orig_path.pic_mean
        temp[pic] = [orig_mean]

        for compare in temp:
            if pic != compare:
                comp_path = Picture(root, compare)
                comp_mean = comp_path.pic_mean

                if orig_mean == comp_mean:
                    dupe = comp_path.pic_path
                    yield pic, dupe


def main():
    """This function is used for testing within the module itself only!"""
    for i in find_dupes(CHOSEN_PATH):
        print(i)
    # delete = []
    # for i in find_dupes(CHOSEN_PATH):
    #     print(f"Original file {i[0]} has a duplicate file at location {i[1]}")
    #     if i[1] not in delete:
    #         delete.append(i[1])


if __name__ == "__main__":
    main()
