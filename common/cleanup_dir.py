import os

def cleanup_dir(directory, file_expressions):
    """
    Cleans up the specified directory by deleting files matching the given expressions.

    Args:
        directory (str): The directory path to clean.
        file_expressions (list): A list of file expressions to match.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If there is a permission issue while accessing or deleting files.
        OSError: If any other error occurs during file deletion.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    try:
        file_list = os.listdir(directory)  # Get the list of files in the directory
    except (PermissionError, OSError) as e:
        raise e

    for expression in file_expressions:
        if expression == '*.*':
            files_to_delete = file_list  # Delete all files
        else:
            files_to_delete = [file_name for file_name in file_list if file_name.endswith(expression)]

        for file_name in files_to_delete:
            file_path = os.path.join(directory, file_name)
            try:
                os.remove(file_path)  # Delete the file
            except (PermissionError, OSError) as e:
                raise e
