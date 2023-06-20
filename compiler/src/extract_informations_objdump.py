import json
import os
import shutil
from .abstract_step import AbstractStep
from .invoker import Invoker


class ExtractInformationsObjdump(AbstractStep):
    """
    A step that extracts information using the 'objdump' command.
    """

    def run(self):
        # Call the obj_dump method to extract information for the ".flash" section
        self.obj_dump(".flash")
        # Call the obj_dump method for other sections if needed
        # self.obj_dump(".sdata")
        # self.obj_dump(".sdata2")

        # Call the obj_dump method without specifying a section to extract information for the entire object file
        # self.obj_dump()

    def obj_dump(self, section=None):
        # Prepare the arguments for the objdump command
        args = ["-d", "code.elf"]
        if section:
            args.append("-j")
            args.append(section)
        # Create an instance of the Invoker class with the working directory
        invoker = Invoker(self.workdir)
        # Invoke the objdump command with the specified arguments and command
        returncode, stdout, stderr = invoker.invoke_gcc(*args, cmd="objdump.exe")
        # Print the output of objdump
        print(stdout)
