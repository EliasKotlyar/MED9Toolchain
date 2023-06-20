from .abstract_step import AbstractStep
from .invoker import Invoker


class ExtractSectionInformationsNm(AbstractStep):
    """
    A step that extracts section information using the 'nm' command.
    """

    def run(self):
        # Call the nm command to extract section information
        self.call_nm()

    def call_nm(self):
        # Specify the input file for nm command
        args = ["section.elf"]
        # Create an instance of the Invoker class with the working directory
        invoker = Invoker(self.workdir)
        # Invoke the nm command with the specified arguments and command
        returncode, stdout, stderr = invoker.invoke_gcc(*args, cmd="nm.exe")
        # Parse the nm output to extract symbols
        nm_arr = self.parse_nm_output(stdout)
        return nm_arr

    def parse_nm_output(self, output: str):
        symbols = []
        lines = output.strip().split("\n")
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                address, symbol_type, symbol_name = parts[:3]
                symbol = {
                    "address": address,
                    "type": symbol_type,
                    "name": symbol_name
                }
                forbidden_symbols = ["__SBSS2_END__", "__SBSS2_START__", "__SDATA2_END__", "__SDATA2_START__",
                                     "_SDA2_BASE_"]
                if symbol_name in forbidden_symbols:
                    continue
                symbols.append(symbol)
        return symbols
