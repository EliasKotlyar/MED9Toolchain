from .abstract_step import AbstractStep
from .invoker import Invoker


class CopyFlashSection(AbstractStep):
    """
    A step that copies the flash section from the 'code.elf' file to a binary file named 'flashsection.bin'.
    """

    def run(self):
        # Specify the name of the flash section
        section_name = ".flash"
        # Specify the output file name for the copied flash section
        output_file = "flashsection.bin"
        # Specify the input file (code.elf) from which the flash section will be copied
        input_file = "code.elf"
        # Define the command-line arguments for the objcopy command
        args = ['-O', "binary", f"--only-section={section_name}", input_file, output_file]
        # Create an instance of the Invoker class with the working directory
        invoker = Invoker(self.workdir)
        # Invoke the objcopy command with the specified arguments and command
        invoker.invoke_gcc(*args, cmd="objcopy.exe")
