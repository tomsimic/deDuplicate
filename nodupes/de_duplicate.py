"""
Author: Tom Simic
Date: 2024-08-03
Purpouse: Search for duplicate pictures in all directories and decide to
delete them automatically or just get the list of full paths of duplicate files
"""
# Pseudo code:
# import needed modules
# set constants
# check for folders within folder and create a list of directories
#

# Importing needed modules:
import os
import timeit
from datetime import datetime, timedelta
from PIL import Image, ImageStat, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


# Constants
test_PATH = r'C:\Users\totalyscrewedup\Pictures'
# test_PATH = r'C:\Users\totalyscrewedup\Pictures\deDuplicateTestPics'
# test_PATH = r'C:\Users\totalyscrewedup\Pictures'
FILE_TYPE = ('.png', '.jpg')  # augment later for user's selection
TOTAL = 0


# Test function:
def folder_recursion(root, suffix):
    """Checking directory for subdirectories."""
    # results = ([os.path.join(root, file) for file in files]
    #            for root, _, files in os.walk(root))
    # content = []
    # for root, directories, files in os.walk(root):
    #     # if directories:
    #     #     # print("Directories found in ", root)
    #     #     for directory in directories:
    #     #         # print(os.path.join(root, directory))
    #     #         dirs.append(os.path.join(root, directory))
    #     if files:
    #         for file in files:
    #             content.append(os.path.join(root, file))
    # return results
    return ([os.path.join(root, file) for file in files if file.endswith
             (suffix)] for root, _, files in os.walk(root))


def duplicates(root):
    """Comparing the mean value of each picture in the directory structure."""

    def get_mean(picture):
        return tuple(ImageStat.Stat(Image.open(picture)).mean)

    opened, failed, res, test, dupes, total = [], [], [], {}, {}, 0
    for pic in root:
        try:
            pic_mean = get_mean(pic)
            test[pic] = pic_mean
            opened.append(pic)
            print(pic)
        except OSError:
            failed.append(f"Failed to load -> {pic}")
            print(f"Failed to load {pic} but continuing to next picture. Please wait.")
        except:
            failed.append("Don't know what happened.")
            print("Don't know what went wrong")

        for ck_pic in test:
            if pic != ck_pic:
                ck_pic_mean = test.get(ck_pic)
                if pic_mean == ck_pic_mean:
                    dupes[ck_pic] = pic,
                    if pic not in res:
                        res.append(pic)
                        total += 1
    return failed, len(opened), res, dupes, total

start = datetime.now()

all_files = (file for subdirectory in folder_recursion(
    test_PATH, FILE_TYPE) for file in subdirectory)


def main():
    """Executes the main program."""
    print("Program started:", start)
    print("Comparing pictures now. \
This might take a while. Please be patient...")
    failed, tested, results, my_set, total = duplicates(all_files)
        
    if total < 1:
        print("No duplicates found. Goodbye!")
        return
    else:
        print("Total of duplicates across all folders found:", total)
        print("Files to be erased should be:")
        for picture in results:
            print(picture)

        print(len(results))
        # print(my_set)
        print(f"Scanned a total of {tested} files")
        end = datetime.now() 
        with open(os.path.join(test_PATH, 'results.txt'), 'w', newline="", encoding="UTF-8") as f:
            delete = input("Do you want to delete the located duplicates \
    automatically?\nWARNING!!!!! This is not reversable as the items will be \
    deleted permanently!!!\nPlease enter Yes or any other key for now, followed by\
    Enter key.> ")
            f.write("Following duplicates found:\n")
            for file in results:
                f.write(file + '\n')
            f.write("Following failed:\n")
            for fail in failed:
                f.write(fail + '\n')
            if delete.lower() == "yes":
                f.write("You've opted to have the items deleted and those items were:\n")
                print("You've elected to delete the pictures automatically. Executing now. Please wait...")
                for picture in results:
                    f.write(str(picture) + '\n')
                    if os.path.exists(picture):
                        print(f"Deleting {picture} picture now.")
                        os.remove(picture)
            else:
                f.write("The files to visually compare should be:\n")
                for key, value in my_set.items():
                    f.write(f"{key} ===> {value}.\n")
        print(f"A CSV file named results.txt has been generated in the {
            test_PATH} search directory for your conviniance.")
        print("Task completed successfully")
        duration = (end - start).total_seconds()
        delta = timedelta(seconds=duration)
        print(f"The program ran for {duration:.02f} seconds")
        print(f"Elapsed time:\n {delta}")


if __name__ == "__main__":
    main()
    # print(timeit.timeit(stmt='duplicates(all_files)', setup='', number=10, globals=globals()))
