import re


# This class provides methods for finding addresses based on regular expressions.
class AddressFinderRegExp:
    def __init__(self, file_content: str):
        # Constructor method for the AddressFinderRegExp class.
        # It takes the file content as input, which should be in hexadecimal format.
        self.file_content = file_content

    def find_by_signature(self, signature: str):
        # Method for finding an address based on a signature.
        # It takes a signature string as input and returns the address.
        signature = signature.upper()
        _signature = signature.replace("X", "[0-9A-F]{1}")
        _signature = _signature.replace(" ", "")
        pattern = re.compile(_signature)
        matches = re.findall(pattern, self.file_content)

        if len(matches) == 0:
            raise ValueError(f'Signature "{signature}" not found.')

        if len(matches) > 1:
            raise ValueError(f'Signature "{signature}" found multiple times.')

        return self.file_content.find(matches[0]) // 2

    def pick_short(self, address: int):
        # Method for picking a short value (2 bytes) at a given address.
        # It takes the address as input and returns the short value.
        start_index = address * 2
        end_index = start_index + 4  # Two bytes, each represented by two characters

        selected_bytes = self.file_content[start_index:end_index]

        return int(selected_bytes, 16)

    def pick_long(self, address: int):
        # Method for picking a long value (4 bytes) at a given address.
        # It takes the address as input and returns the long value.
        start_index = address * 2
        end_index = start_index + 8  # Four bytes, each represented by two characters

        selected_bytes = self.file_content[start_index:end_index]

        return int(selected_bytes, 32)
