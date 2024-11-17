import os

def rename_files(directory):
    files = os.listdir(directory)
    files.sort()  # Sort files to ensure consistent ordering
    for index, filename in enumerate(files):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{index}{file_extension}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

# Paths to the directories
dog_directory = "./dataset/val/dog"
cat_directory = "./dataset/val/cat"

# Rename files in both directories
rename_files(dog_directory)
rename_files(cat_directory)