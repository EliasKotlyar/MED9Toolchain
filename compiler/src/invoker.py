import os
import subprocess


class Invoker:
    """
    A utility class for invoking GCC commands.
    """

    def __init__(self, workdir: str):
        self.gcc_base = r"C:\SysGCC\powerpc-eabi\bin\powerpc-eabi-"
        self.check_gcc_exists()
        self.working_dir = workdir

    def check_gcc_exists(self):
        # Check if the GCC executable exists
        gcc_path = self.gcc_base + "gcc.exe"
        if not os.path.exists(gcc_path):
            raise FileNotFoundError("gcc not found. Please provide a proper path in " + __file__)

    def invoke_gcc(self, *args, cmd="gcc.exe"):
        # Invoke the GCC command with the specified arguments and command
        gcc_path = self.gcc_base + cmd
        command = [gcc_path, *args]

        returncode, stdout, stderr = self.run_command(command)
        if returncode != 0:
            # Print command, stdout, and stderr if the invocation failed
            print(command)
            print(stdout)
            print(stderr)
            raise Exception("Invocation failed with return code: " + str(returncode))
        return returncode, stdout, stderr

    def run_command(self, command: str):
        # Run the given command in the working directory
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                   cwd=self.working_dir)
        stdout, stderr = process.communicate()
        stdout = stdout.decode('utf-8').strip()
        stderr = stderr.decode('utf-8').strip()
        return process.returncode, stdout, stderr
