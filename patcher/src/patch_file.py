import os

from common.read_binary_file import read_binary_file
from common.read_json_file import read_json_file
from common.write_binary_file import write_binary_file
from patcher.src.power_pc_assembler import PowerPCAssembler


class PatchFile:
    def __init__(self, workdir):
        self.workdir = workdir
        file_content = read_binary_file(os.path.abspath(self.workdir + "/input.bin"))
        self.content = file_content
        self.analysis = read_json_file(os.path.abspath(self.workdir + "/analysis.json"))
        self.memorymap = read_json_file(os.path.abspath(self.workdir + "/memorymap.json"))
        self.assembler = PowerPCAssembler()
        self.outputfile = os.path.abspath(self.workdir + "/output.bin")

        return

    def get_analysis(self, name: str) -> str:
        return self.analysis[name]
        pass

    def get_memorymap(self, name: str) -> str:
        return self.memorymap[name]
        pass

    def write_file(self):
        write_binary_file(self.outputfile, self.content)

    def write_bytes(self, address_hex: str, value_bytes: str):
        address = int(address_hex, 16) * 2

        # Check if the address is within the bounds of the content
        if address < 0 or address >= len(self.content):
            raise ValueError("Address is out of bounds")

        # Calculate the end address based on the value length
        end_address = address + len(value_bytes)

        # Check if the end address is within the bounds of the content
        if end_address > len(self.content):
            raise ValueError("Value exceeds the length of the content")

        self.content = self.content[:address] + value_bytes + self.content[address + len(value_bytes):]

    def write_long(self, address: str, value: int):
        value_bytes = value.to_bytes(4, 'big')
        value_bytes = value_bytes.hex().upper()
        self.write_bytes(address, value_bytes)

    def assemble(self, string):
        return self.assembler.assemble_from_list(string)

    def writeCode(self):
        memoryAddr = self.get_analysis('FREE_FLASH_MEMORY')
        memoryAddr = int(memoryAddr, 16)
        memoryAddr -= 0x400000
        memoryAddr = hex(memoryAddr).upper()

        file_content = read_binary_file(os.path.abspath(self.workdir + "/flash.bin"))
        self.write_bytes(memoryAddr, file_content)
