import argparse
import os
import shutil

from analysis.analyser import Analyser
from common.cleanup_dir import cleanup_dir
from compiler.compiler import Compiler
from patcher.patcher import Patcher


class Med9Toolchain:
    def __init__(self, inputfile: str, outputfile: [] = None, patches_to_apply: [] = None):
        self.inputfile = os.path.abspath(inputfile)
        self.outputfile = os.path.abspath(outputfile)
        self.patches = patches_to_apply
        self.workdir = os.path.abspath("work/")

    def apply_patches(self):
        files_to_delete = ['*.*']
        cleanup_dir(self.workdir, files_to_delete)
        # Copy File as input bin:
        inp_file = os.path.abspath(self.workdir + "/input.bin")
        shutil.copy(self.inputfile, inp_file)
        # Analyse file:
        analyser = Analyser()
        analyser.process_file(inp_file, os.path.abspath(self.workdir + "/analysis.json"))
        # Add all C-Files into the workdir to be able to compile them:
        patcher = Patcher(self.workdir, self.patches)
        patcher.copy_c_files()
        # Compile everything together:
        compiler = Compiler(self.workdir)
        compiler.compile()
        # Apply all patches:
        patcher.apply_patches()
        # Copy file back:
        generated_file = os.path.abspath(self.workdir + "/output.bin")
        shutil.copy(generated_file, self.outputfile)
        pass

    def run(self):
        # Check if the input file exists

        # Call the method to apply the patch
        self.apply_patches()

        print("Patch applied successfully.")


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="med9toolchain - Apply patch to a file")

    parser.add_argument("inputfile", help="path to the input file", type=str)
    parser.add_argument("-o", "--outputfile", help="path to the output file", type=str)

    patches = Patcher.get_available_patches()
    parser.add_argument(
        'patches',
        nargs='*',
        help='List of patches to apply',
        choices=patches,
    )

    # Parse the arguments
    args = parser.parse_args()

    if not args.patches:
        parser.print_help()
        patches_help = '\nAvailable patches:\n' + '\n'.join(['- ' + patch for patch in patches])
        print(patches_help)
        exit(0)

    if not os.path.exists(args.inputfile):
        print("Error: Input file does not exist.")
        exit(-1)

        # Set the default output file if not provided
    if not args.outputfile:
        args.outputfile = args.inputfile + "_MOD.bin"
    # Create an instance of Med9Toolchain
    toolchain = Med9Toolchain(args.inputfile, args.outputfile, args.patches)

    # Run the toolchain
    toolchain.run()
