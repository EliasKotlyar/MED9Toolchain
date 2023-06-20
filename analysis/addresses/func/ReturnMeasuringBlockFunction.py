from analysis.addresses.abstract_addressprovider import AbstractAddressProvider


# This class represents a function used as a return point of measuring blocks.
# It extends the AbstractAddressProvider class.
class ReturnMeasuringBlockFunction(AbstractAddressProvider):

    def getAddress(self) -> str:
        # Assembly instructions for generating the function's address.
        # li      r3, 0x25
        signature = "38 60 00 25"
        # li         r4,0x0
        signature += "38 80 00 00"
        # addi         r5, r4, 0x0
        signature += "38 a4 00 00"
        #  b          Back Func
        signature += "4b ff ff e4"

        # Use the bit_mask_finder object to find the address based on the signature.
        sigAddress = self.bit_mask_finder.find_by_signature(signature)

        # Minus 28 - relative Jump
        sigAddress -= 28

        # Return the hexadecimal representation of the calculated address.
        return hex(sigAddress)

    def getValues(self) -> []:
        # Return a dictionary of values, with the key "FUNC_RET_MEASUREMENT_BLOCKS"
        # mapped to the address obtained from the getAddress method.
        return {
            "FUNC_RET_MEASUREMENT_BLOCKS": self.getAddress()
        }
