import os

from common.write_json_file import write_json_file
from .abstract_step import AbstractStep
from .invoker import Invoker


class ExtractFlashBin(AbstractStep):
    """
    A step that extracts section information using the 'readelf' command.
    """

    def run(self):
        # Initialize a list to store the extracted information
        ret = {}
        self.dump_section(".flash", "flash.bin")

    def dump_section(self, section_name: str, output_file: str):
        # Specify the output and input files for objcopy command
        input_file = "code.elf"
        args = [f"--only-section={section_name}", input_file, "-O", "binary", output_file]
        # Create an instance of the Invoker class with the working directory
        invoker = Invoker(self.workdir)
        # Invoke the objcopy command with the specified arguments and command
        invoker.invoke_gcc(*args, cmd="objcopy.exe")
