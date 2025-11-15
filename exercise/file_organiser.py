import os
import shutil

#directory = os.path.join(os.path.expanduser("~"), "OneDrive", "Esma-personlig", "Skrivebord", "alt_piss",)
directory = r"C:\Users\esmab\OneDrive\Bilder"

extensions = {
    ".jpg": "bilder_1",
    ".png": "bilder_1",
    ".gif": "bilder_1",
    ".mp4": "video_1",
    ".docx": "word_filer",
    ".pdf": "pdf_filer",
    ".3mf": "3d_printing",
    ".pptx": "powerpointer",
    ".AVI": "video_1"
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok = True)
            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"skipped {filename}. Unknown file extension")
    else:
        print(f"Skipped {filename}, it is a directory")
