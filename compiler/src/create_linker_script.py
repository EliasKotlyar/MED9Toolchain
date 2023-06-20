import json
import os
from typing import List

from common.read_json_file import read_json_file
from .abstract_step import AbstractStep


class CreateLinkerScript(AbstractStep):
    def run(self):
        # Implementation of the run method from the AbstractStep class.
        # It performs the linker script creation process by calling the necessary methods.

        values = self.parse_analysis()  # Parse the analysis.json file
        self.check_values_in_array(["FREE_FLASH_MEMORY", "FREE_RAM_MEMORY"],
                                   values)  # Check if required variables exist
        self.createLinkerScript(values)  # Create the linker script

    def check_values_in_array(self, required_data: str, variables: List[str]):
        # Method for checking if required variables exist in the analyzed variables dictionary.
        # It takes a list of required data and the variables dictionary as input.

        for value in required_data:
            if value not in variables:
                raise ValueError(f"Error: Variable '{value}' is required for the compilation to work")

    def createLinkerScript(self, values: []):
        # Method for creating the linker script based on the analyzed variables.
        # It takes the variables dictionary as input and replaces the variable placeholders in the linker script template.

        c_code_dir = os.path.dirname(__file__)
        c_code_dir = os.path.join(c_code_dir, "../c-code/")
        linker_file = os.path.abspath(c_code_dir + "/linker.txt")

        with open(linker_file, 'r') as file:
            template = file.read()  # Read the linker script template

        formatted_script = self.replace_variables(template, values)  # Replace variable placeholders with actual values

        linker_script = os.path.join(self.workdir, 'linker.txt')  # Path to the linker script file
        with open(linker_script, 'w') as file:
            file.write(formatted_script)  # Write the formatted linker script to the file

    def replace_variables(self, string, variables):
        # Method for replacing variable placeholders in a string with actual values.
        # It takes a string and a variables dictionary as input and performs the replacement.

        for variable, value in variables.items():
            string = string.replace(variable, str(value))

        return string
