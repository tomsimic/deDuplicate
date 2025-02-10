"""
Author: Tom Simic
Date: 2024-08-01
Purpouse: Returns mean value for a picture
"""
# Pseudo code:
# import needed modules
# create Picture dataclass
# create main function for testing
# name/main if statement
import os
from dataclasses import dataclass, field
from PIL import Image, ImageStat


@dataclass(slots=True)
class Picture:
    """Returns full path and mean value of the picture."""
    location: str
    pic_name: str
    pic_path: str = field(init=False)
    pic_mean: list[str] = field(init=False, default_factory=list)
    _pic: bytearray = field(init=False)

    def __post_init__(self) -> None:
        self.pic_path = os.path.join(self.location, self.pic_name)
        self._pic = Image.open(self.pic_path)
        self.pic_mean = ImageStat.Stat(self._pic).mean


def main() -> None:
    """Test function only!!!"""
    picture = Picture(
        r'C:\Users\totalyscrewedup\Pictures\deDuplicateTestPics', 'profile_2.jpg')
    print(picture.pic_path, picture.pic_mean)


if __name__ == "__main__":
    main()
