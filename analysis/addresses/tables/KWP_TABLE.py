from analysis.addresses.abstract_addressprovider import AbstractAddressProvider


# This class represents the LDRXN Tables.
# It extends the AbstractAddressProvider class.
class KWP_TABLE(AbstractAddressProvider):
    '''
    Get Values
    '''

    def get_variant1(self) -> []:
        # Create a signature string for the KWP Table.
        signature = "20 ff ff ff"
        signature += "00 00 00 XX"
        signature += "00 XX XX XX"
        signature += "00 00 00 00"
        signature += "00 00 00 00"
        return self.bit_mask_finder.find_by_signature(signature)

    def get_variant2(self) -> []:
        # Create a signature string for the KWP Table.
        signature = "20 ff ff ff"
        signature += "FF FF FF FF"
        signature += "00 XX XX XX"
        signature += "00 00 00 00"
        signature += "00 00 00 00"
        signature += "01 ff ff ff"
        return self.bit_mask_finder.find_by_signature(signature)

    def getValues(self):

        try:
            table_entry_signature_address = self.get_variant1()
        except ValueError:
            table_entry_signature_address = self.get_variant2()
        table_entry_signature_address += 20
        return {
            "KWP_TABLE": hex(table_entry_signature_address),
        }
