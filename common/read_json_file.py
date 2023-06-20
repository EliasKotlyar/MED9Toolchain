import json
import os


def read_json_file(file):


    # Check if the analysis file exists
    if not os.path.isfile(file):
        raise Exception('Input file "analysis.json" not found in the specified working directory.')

    # Read the JSON file
    with open(file, 'r') as file:
        try:
            variables = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Error: Invalid JSON file")

    return variables
