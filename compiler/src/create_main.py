import json
import os
import shutil

from common.copy_file import copy_file
from .abstract_step import AbstractStep


class CreateMain(AbstractStep):
    def run(self):
        # Implementation of the run method from the AbstractStep class.
        # It performs the creation of the main.c file by copying it from the source to the destination.

        c_code_dir = os.path.dirname(__file__)
        c_code_dir = os.path.join(c_code_dir, "../c-code/")
        main_file = os.path.abspath(c_code_dir + "/main.c")

        main_c = os.path.join(self.workdir, 'main.c')  # Destination path for the main.c file
        copy_file(main_file, main_c)  # Copy the main.c file from source to destination
