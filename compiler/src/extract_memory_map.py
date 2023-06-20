import os

from common.write_json_file import write_json_file
from .abstract_step import AbstractStep
from .invoker import Invoker


class ExtractMemoryMap(AbstractStep):
    """
    A step that extracts section information using the 'readelf' command.
    """

    def run(self):
        # Initialize a list to store the extracted information
        ret = {}
        self.copy_section_to_elf(".flash", "section_flash.elf")
        self.copy_section_to_elf(".ram", "section_ram.elf")
        # Copy and extract information for the ".flash" section
        ret.update(self.call_readelf("section_flash.elf"))
        # Copy and extract information for the ".ram" section
        ret.update(self.call_readelf("section_ram.elf"))

        print("Memory Map:")
        print(ret)

        memory_map_file = os.path.abspath(self.workdir + "/memorymap.json")
        write_json_file(memory_map_file, ret)

    def copy_section_to_elf(self, section_name: str, output_file: str):
        # Specify the output and input files for objcopy command
        input_file = "code.elf"
        args = [f"--only-section={section_name}", input_file, output_file]
        # Create an instance of the Invoker class with the working directory
        invoker = Invoker(self.workdir)
        # Invoke the objcopy command with the specified arguments and command
        invoker.invoke_gcc(*args, cmd="objcopy.exe")

    def call_readelf(self, input_file: str):
        # Specify the input file for readelf command
        args = ["-s", input_file]
        # Create an instance of the Invoker class with the working directory
        invoker = Invoker(self.workdir)
        # Invoke the readelf command with the specified arguments and command
        returncode, stdout, stderr = invoker.invoke_gcc(*args, cmd="readelf.exe")
        # Parse the readelf output to extract symbol table
        readelf_arr = self.parse_readelf_output(stdout)
        return readelf_arr

    def parse_readelf_output(self, readelf_output: str):
        symbol_table = {}
        lines = readelf_output.strip().split("\n")
        for line in lines[3:]:
            line_parts = line.strip().split()
            if len(line_parts) >= 8:
                address = line_parts[1]
                size = line_parts[2]
                symbol_type = line_parts[3]
                bind = line_parts[4]
                vis = line_parts[5]
                section_index = line_parts[6]
                name = line_parts[7]

                symbol = {
                    "address": address,
                    "size": size,
                    "type": symbol_type,
                    "bind": bind,
                    "visibility": vis,
                    "section_index": section_index,
                    "name": name
                }
                forbidden_symbols = ["__SBSS2_END__", "__SBSS2_START__", "__SDATA2_END__", "__SDATA2_START__",
                                     "_SDA2_BASE_", "", "header", "footer"]
                if name in forbidden_symbols:
                    continue
                if symbol_type == "OBJECT":
                    type = "VAR_"
                elif symbol_type == "FUNC":
                    type = "FUNC_"
                else:
                    continue
                address = "0x" + symbol["address"]
                key = type + symbol["name"]
                symbol_table[key] = address

        return symbol_table
