from analysis.addresses.abstract_addressprovider import AbstractAddressProvider


# This class represents the BFGREN variable for Cruise Control on/off (byte value).
# It extends the AbstractAddressProvider class.
class BFGREN(AbstractAddressProvider):

    def getAddress(self) -> str:
        # Create a signature string to find the address of the BFGREN variable.
        # Entry before the Bgren
        signature = "3b f9 00 00" \
                    "48 00 00 08" \
                    "57 7f 04 3e"
        signature += "b3 ed XX XX"
        signature += "8b 6d XX XX"

        # Use the bit_mask_finder object to find the address based on the signature.
        sigAddress = self.bit_mask_finder.find_by_signature(signature)
        # Plus 18, to get to the LBZ instruction target:
        sigAddress += 18
        # Pick the short value at the target address:
        shortValue = self.bit_mask_finder.pick_short(sigAddress)
        # Add the R13 value to it:
        shortValue += 0x7ffff0

        # Return the hexadecimal representation of the calculated address.
        return hex(shortValue)

    def getValues(self) -> []:
        # Return a dictionary of values, with the key "VAR_BFGREN"
        # mapped to the address obtained from the getAddress method.
        return {
            "VAR_BFGREN": self.getAddress()
        }
