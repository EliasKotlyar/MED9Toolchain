import json


def write_json_file(outputfile: str, content):
    # Method for writing content as JSON to a file.
    # It takes the output file path and the content as input.
    try:
        with open(outputfile, 'w') as f:
            # Write the content as JSON to the output file
            json.dump(content, f, indent=4)

        print(f"Content written as JSON to '{outputfile}' successfully.")

    except IOError:
        print(f"Error: Failed to write content to '{outputfile}'.")
