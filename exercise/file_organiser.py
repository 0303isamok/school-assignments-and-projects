import os
import shutil

#Place File-adress.
directory = r""

#Make your own folders and name them below.
extensions = {
    ".jpg": "folder name",
    ".png": "folder name",
    ".gif": "folder name",
    ".mp4": "folder name",
    ".docx": "folder name",
    ".pdf": "folder name",
    ".3mf": "folder name",
    ".pptx": "folder name",
    ".AVI": "folder name"
}

for name_file in os.listdir(directory):
    file_path = os.path.join(directory, name_file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(name_file)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok = True)
            destination_path = os.path.join(folder_path, name_file)
            shutil.move(file_path, destination_path)

            print(f"Moved {name_file} to {folder_name} folder.")
        else:
            print(f"skipped {name_file}. Unknown file extension")
    else:
        print(f"Skipped {name_file}, it is a directory")
