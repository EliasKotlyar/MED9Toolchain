import argparse

from compiler.src.abstract_step import AbstractStep
from compiler.src.cleanup import CleanUp
from compiler.src.compile import Compile
from compiler.src.create_header import CreateHeader
from compiler.src.create_linker_script import CreateLinkerScript
from compiler.src.create_main import CreateMain
from compiler.src.extract_flash_bin import ExtractFlashBin
from compiler.src.extract_informations_objdump import ExtractInformationsObjdump
from compiler.src.extract_memory_map import ExtractMemoryMap


class Compiler:
    def __init__(self, workdir):
        self.workdir = workdir

    def compile(self):
        steps = [
            CleanUp,
            CreateLinkerScript,
            CreateHeader,
            CreateMain,
            Compile,
            ExtractInformationsObjdump,
            ExtractMemoryMap,
            ExtractFlashBin,

        ]

        for class_object in steps:
            step: AbstractStep = class_object(self.workdir)
            step.run()


if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Process input file and generate output file.')

    # Add argument for work directory
    parser.add_argument('workdir', help='path to the working directory', default='./../work', nargs='?')

    # Parse the command line arguments
    args = parser.parse_args()

    # Create a Compiler instance with the JSON file path
    compiler = Compiler(args.workdir)
    compiler.compile()
