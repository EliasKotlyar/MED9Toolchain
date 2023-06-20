import json
import os

from common.read_json_file import read_json_file


class AbstractStep:
    def __init__(self, workdir: str):
        # Constructor for the AbstractStep class.
        # It takes the working directory path as input and assigns it to the instance variable.

        self.workdir = workdir

    def run(self):
        # Abstract method for running the step.
        # Subclasses must implement this method.
        raise NotImplementedError("Subclasses must implement the run method.")

    def parse_analysis(self):
        linker_file = os.path.abspath(self.workdir + "/analysis.json")
        return read_json_file(linker_file)
