def write_binary_file(outputfile: str, content: str):
    """
    Writes the provided hex string content to a binary file.

    Args:
        outputfile (str): The name or path of the output binary file.
        content (str): The hex string content to write to the file.

    Returns:
        None
    """
    # Convert the hex string to bytes
    binary_content = bytes.fromhex(content)

    with open(outputfile, "wb") as file:
        file.write(binary_content)
