import importlib
import os
import sys
from typing import List

from common.create_file_list import create_file_list
from common.load_python_file import load_python_file
from .abstract_patch import AbstractPatch


class CollectPatches:
    def collect(self) -> List[AbstractPatch]:
        patch_dir = os.path.dirname(os.path.abspath(__file__))
        patch_dir = os.path.join(patch_dir, "../patches/")
        patch_dir = os.path.abspath(patch_dir)
        files = create_file_list(patch_dir, ".py")

        # Create an empty dictionary to store the values
        patch_list = []

        # Iterate through the address finder files
        for file in files:
            # Get the class object from the file
            obj = load_python_file(file, AbstractPatch)
            # If no class object is found, continue to the next file
            if obj is None:
                continue
            obj = obj()

            patch_list.append(obj)
        return patch_list
