"""
Author: Tom Simic
Date: 2024-08-01
Purpouse: Returns mean value for a picture
"""
from PIL import ImageStat
# Create Mean class


class Mean:
    def __init__(self, pic_loc):
        self._pic_loc = pic_loc

    def getMean(self):
        return ImageStat.Stat(self._pic_loc).mean


if __name__ == "__main__":
    # This is used for testing only:
    from PIL import Image
    test_path = r'C:\Users\totalyscrewedup\Pictures\deDuplicateTestPics\profile_2.jpg'
    pic = Mean(Image.open(test_path))
    print("Pic's details:", pic._pic_loc)
    print("Pic's mean values:", pic.getMean())
