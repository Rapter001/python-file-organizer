import os
import shutil

def organize_files(directory):
    other_folder = os.path.join(directory, 'other')
    if not os.path.exists(other_folder):
        os.makedirs(other_folder)

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            # File handling
            file_extension = os.path.splitext(item)[1][1:]  # Get the file extension without the dot
            dest_path = os.path.join(directory, file_extension, item)

            if file_extension:
                # Move the file to the corresponding folder based on its extension
                if not os.path.exists(os.path.join(directory, file_extension)):
                    os.makedirs(os.path.join(directory, file_extension))
                shutil.move(item_path, dest_path)
            else:
                # Move files without extensions to the "Other" folder
                shutil.move(item_path, os.path.join(other_folder, item))
        elif os.path.isdir(item_path):
            # Move folders to the "Other" folder
            if item != 'Other':
                shutil.move(item_path, os.path.join(other_folder, item))

    print('File and folder organization completed.')

# Ask for the directory to organize
directory_path = input("Enter the directory path to organize: ")
organize_files(directory_path)
