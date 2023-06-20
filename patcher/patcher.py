import argparse
import importlib
import os
import shutil
import sys

from common.load_python_file import get_python_file_from_obj
from common.write_binary_file import write_binary_file
from patcher.src import collect_patches
from patcher.src.abstract_patch import AbstractPatch
import inspect

from patcher.src.collect_patches import CollectPatches
from patcher.src.patch_file import PatchFile


class Patcher:
    def __init__(self, workdir='./work', patches_to_apply=[]):
        self.workdir = os.path.abspath(workdir)
        patch_collector = CollectPatches()
        self.available_patches = patch_collector.collect()
        self.patches = []
        for name in patches_to_apply:
            self.patches.append(self.get_patch_by_name(name))

    def get_patch_by_name(self, patch_name) -> AbstractPatch:
        for patch in self.available_patches:
            if patch_name == patch.get_name():
                return patch
        raise Exception("Patch not found!")

    def patch_file(self, patches_names):
        patches = []
        for name in patches_names:
            patches.append(self.get_patch_by_name(name))
        # Analyse File:
        print(patches)
        pass

    def get_patch_directory(self, patch: AbstractPatch) -> str:
        filename = get_python_file_from_obj(patch)
        dirname = os.path.dirname(filename)
        return dirname

    def copy_c_files(self):
        for patch in self.patches:
            patch_dir = self.get_patch_directory(patch)
            for fileName in patch.get_c_files():
                c_file_src = os.path.join(patch_dir, fileName)
                c_file_dest = os.path.join(self.workdir, fileName)
                shutil.copy(c_file_src, c_file_dest)

    @staticmethod
    def get_available_patches():
        patch_collector = CollectPatches()
        patch_names = []
        for patch in patch_collector.collect():
            patch_names.append(patch.get_name())
        return patch_names

    def apply_patches(self):
        file = PatchFile(self.workdir)
        for patch in self.patches:
            patch.setFile(file)
            patch.apply_patch()
        # Patch code changes:
        file.writeCode()
        # Write into "output.bin"
        file.write_file()


if __name__ == '__main__':
    # Create an instance of the Analyser class
    patcher = Patcher()
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Process input file and generate output file.')

    # Add argument for work directory

    # Add 'patch' argument
    patches = patcher.get_available_patches()
    parser.add_argument(
        'patches',
        nargs='*',
        help='List of patches to apply',
        choices=patches,
    )
    parser.add_argument('-w', help='Workdir', default='./../work', dest="workdir")

    # Parse the command line arguments
    args = parser.parse_args()

    if not args.patches:
        parser.print_help()

        patches_help = '\nAvailable patches:\n' + '\n'.join(['- ' + patch for patch in patches])
        print(patches_help)
        exit(0)
    # Check if "input.bin" exists in the work directory
    input_file = os.path.join(args.workdir, 'code.bin')
    if not os.path.isfile(input_file):
        raise Exception('Input file "code.bin" not found in the specified working directory.')

    # Set the output file path to "analysis.json"
    output_file = os.path.join(args.workdir, 'analysis.json')

    # Call the process_file method of the Analyser instance
    patcher.process_file(args.workdir, args.patches)
