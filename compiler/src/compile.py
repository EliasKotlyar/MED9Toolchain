import os

from common.create_file_list import create_file_list
from .invoker import Invoker
from .abstract_step import AbstractStep


class Compile(AbstractStep):

    def run(self):
        # Implementation of the run method from the AbstractStep class.
        # It performs the compilation and linking process by calling the respective methods.

        c_file_list = create_file_list(self.workdir, ".c")
        self.compile_all(c_file_list)
        self.link()

    def compile_all(self, file_list: []):
        # Method for compiling all the files in the given file list.
        # It iterates over the file list and calls the compile_file method for each file.

        for file in file_list:
            self.compile_file(file)

    def compile_file(self, file_name: []):
        # Method for compiling a single file.
        # It takes the file name as input and invokes the GCC compiler with the necessary arguments.

        args = ["-msdata=eabi",
                "-O0",
                "-fno-gnu-tm",
                "-c",
                ]
        args.append(file_name)

        invoker = Invoker(self.workdir)
        invoker.invoke_gcc(*args)

    def link(self):
        # Method for linking the compiled object files.
        # It creates a list of object files in the working directory,
        # and invokes the GCC linker with the necessary arguments to generate the ELF file.

        o_file_list = create_file_list(self.workdir, ".o")
        args = ["-o", "code.elf"]
        args += o_file_list
        args += ["-fno-gnu-tm", "-Wl,--fatal-warnings,-T,linker.txt"]

        invoker = Invoker(self.workdir)
        invoker.invoke_gcc(*args)
