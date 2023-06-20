import os

from analysis.analyser import Analyser
from common.create_file_list import create_file_list


class TestAnalyzer:

    def run(self):
        # Method for running the analysis on multiple files.
        # It creates an instance of the Analyser class and processes each file.

        # Create an instance of the Analyser class
        analyser = Analyser()

        # Create a list of file paths with the '.bin' extension
        file_list = create_file_list("../testfiles/", ".bin")

        # Iterate through the file list
        for file in file_list:
            # Call the process_file method of the Analyser instance for each file
            analyser.process_file(file, file + ".json")


if __name__ == '__main__':
    # Create an instance of the TestAnalyzer class
    analysis = TestAnalyzer()

    # Call the run method of the TestAnalyzer instance
    analysis.run()
