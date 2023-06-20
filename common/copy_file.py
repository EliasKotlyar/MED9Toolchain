import shutil


def copy_file(source: str, destination: str):
    # Method for copying a file from the source path to the destination path.
    # It takes the source and destination paths as input.

    try:
        shutil.copy2(source, destination)  # Copy the file using shutil.copy2
        print(f"File copied successfully from {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied. Unable to copy the file.")
    except Exception as e:
        print(f"An error occurred while copying the file: {str(e)}")
