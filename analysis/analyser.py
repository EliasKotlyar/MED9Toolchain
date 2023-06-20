import importlib
import json
import os
import argparse

from analysis.addresses.abstract_addressprovider import AbstractAddressProvider
from analysis.src.AddressFinderRegExp import AddressFinderRegExp
from common.create_file_list import create_file_list
from common.load_python_file import load_python_file
from common.read_binary_file import read_binary_file
from common.write_json_file import write_json_file


class Analyser:
    def __init__(self):
        # Constructor method for the Analyser class.
        pass


    def process_file(self, inputfile: str, outputfile: str):
        # Method for processing the input file and generating the output file.
        # It takes the input file path and the output file path as input.

        # Read the input file
        file_content = read_binary_file(inputfile)

        # Create an instance of the AddressFinderRegExp class
        bitmaskFinder = AddressFinderRegExp(file_content)

        address_dir = os.path.dirname(__file__)
        address_dir = os.path.join(address_dir, "addresses")
        # Collect address finder files
        files = create_file_list(address_dir, ".py")

        # Create an empty dictionary to store the values
        values = {}

        # Iterate through the address finder files
        for file in files:
            # Get the class object from the file
            obj = load_python_file(file, AbstractAddressProvider)

            # If no class object is found, continue to the next file
            if obj is None:
                continue

            # Create an instance of the address provider class
            address_provider = obj(bitmaskFinder)

            # Call the getValues method of the address provider
            new_values = address_provider.getValues()

            # Update the values dictionary with the new values
            values.update(new_values)

        # Write the values dictionary to the output file
        write_json_file(outputfile, values)


if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Process input file and generate output file.')

    # Add argument for work directory
    parser.add_argument('workdir', help='path to the working directory', default='./../work', nargs='?')

    # Parse the command line arguments
    args = parser.parse_args()

    # Check if "input.bin" exists in the work directory
    input_file = os.path.join(args.workdir, 'input.bin')
    if not os.path.isfile(input_file):
        raise Exception('Input file "input.bin" not found in the specified working directory.')

    # Set the output file path to "analysis.json"
    output_file = os.path.join(args.workdir, 'analysis.json')

    # Create an instance of the Analyser class
    analyser = Analyser()

    # Call the process_file method of the Analyser instance
    analyser.process_file(input_file, output_file)
