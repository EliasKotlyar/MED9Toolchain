from analysis.addresses.abstract_addressprovider import AbstractAddressProvider


# This class represents the TKMWL Table.
# It extends the AbstractAddressProvider class.
class TKMWL(AbstractAddressProvider):

    def getAddress(self) -> str:
        # Create a signature string to find the address of the TKMWL Table.
        # Blr
        signature = "4e 80 00 20"
        # First two bytes of the table:
        signature += "00 03"

        # Use the bit_mask_finder object to find the address based on the signature.
        sigAddress = self.bit_mask_finder.find_by_signature(signature)
        # Plus 4, because of the BLR instruction
        sigAddress += 4

        # Return the hexadecimal representation of the calculated address.
        return hex(sigAddress)

    def getValues(self) -> []:
        # Return a dictionary of values, with the key "TABLE_TKMWL"
        # mapped to the address obtained from the getAddress method.
        return {
            "TABLE_TKMWL": self.getAddress()
        }
