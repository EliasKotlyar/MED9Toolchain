from analysis.addresses.abstract_addressprovider import AbstractAddressProvider


# This class represents the Measuring Blocks Table for KWMWNTK.
# It extends the AbstractAddressProvider class.
class KWMWNTK(AbstractAddressProvider):

    def getAddress(self) -> str:
        # Create a signature string to find the address of the Measuring Blocks Table.
        # First Address Entry before the table
        signature = "00 5C XX XX"
        # First two bytes of the table:
        signature += "00 00"
        # First second byte of the table:
        signature += "00 01"

        # Use the bit_mask_finder object to find the address based on the signature.
        sigAddress = self.bit_mask_finder.find_by_signature(signature)
        # Plus 4, because of the BLR instruction
        sigAddress += 4

        # Return the hexadecimal representation of the calculated address.
        return hex(sigAddress)

    def getValues(self) -> []:
        # Return a dictionary of values, with the key "TABLE_KWMWNTK"
        # mapped to the address obtained from the getAddress method.
        return {
            "TABLE_KWMWNTK": self.getAddress()
        }
