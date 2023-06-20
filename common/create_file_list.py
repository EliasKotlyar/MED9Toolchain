import os
from typing import List


def create_file_list(directory: str, extension: str = ".*") -> List[str]:
    # Method for creating a list of files with a specific extension in a directory.
    # It takes the directory path and the file extension as input and returns a list of file paths.
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    if not file_list:
        raise Exception(f"No files with the '{extension}' extension found in the directory.")

    return file_list
