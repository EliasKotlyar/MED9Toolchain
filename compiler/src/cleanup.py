import glob
import os

from common.cleanup_dir import cleanup_dir
from .abstract_step import AbstractStep


class CleanUp(AbstractStep):

    def run(self):
        # Implementation of the run method from the AbstractStep class.
        # It runs the cleanup process by calling the cleanup method with the files to delete.

        files_to_delete = ['*.elf', '*.o']
        cleanup_dir(self.workdir, files_to_delete)
