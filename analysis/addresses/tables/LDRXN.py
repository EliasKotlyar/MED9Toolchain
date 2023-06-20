from analysis.addresses.abstract_addressprovider import AbstractAddressProvider


# This class represents the LDRXN Tables.
# It extends the AbstractAddressProvider class.
class LDRXN(AbstractAddressProvider):
    '''
    Gets Instruction address, for patching later
    '''

    def get_variant1(self) -> []:
        # Create a signature string for variant 1 of the LDRXN Tables.
        # stw        r3,0x36e0(r13)=>DAT_008036d0
        signature = "90 6d XX XX"
        # lis        r3,0x5d
        signature += "3c 60 00 5d"
        # subi        r3 = > LDRXN, r3, 0x2724
        signature += "38 63 XX XX"
        # lhz        r4,0x35ec(r13)=>NMOTW
        signature += "a0 8d XX XX"
        # bl        FUN_00582b64
        signature += "48 07 XX XX"

        # Use the bit_mask_finder object to find the address of the LDRXN Tables based on the signature.
        ldx_instruction = self.bit_mask_finder.find_by_signature(signature)
        ldx_instruction += 8

        table_ldrxn1 = self.bit_mask_finder.pick_short(ldx_instruction + 2)
        table_ldrxn1 = (0x5c << 16) | table_ldrxn1
        table_ldrxn2 = table_ldrxn1 + 16 * 2
        return ldx_instruction, table_ldrxn1, table_ldrxn2

    def get_variant2(self) -> []:
        # Create a signature string for variant 2 of the LDRXN Tables.
        # lis        r10 ,0x5d
        signature = "3d  40  00  5d"
        # subi      r10 =>PTR_BYTE_005cef44 ,r10 ,0x10bc
        signature += "39  4a  ef  44"
        # rlwinm     r9,r9,0x2 ,0x16 ,0x1d
        signature += "55  29  15  ba"
        # lwzx       r3,r10 =>PTR_BYTE_005cef44 ,r9
        signature += "7c  6a  48  2e"
        # lhz        lhz        r4,-0x27b0 (r13 )=>nMotW_REAL
        signature += "a0 8d XX XX"
        # bl        FUN_00582b64
        signature += "48 07 XX XX"

        # Use the bit_mask_finder object to find the address of the LDRXN Tables based on the signature.
        signature_start = self.bit_mask_finder.find_by_signature(signature)
        ldx_instruction = signature_start + 12

        pointer = self.bit_mask_finder.pick_short(signature_start + 6)
        pointer = (0x5c << 16) | pointer
        pointer = pointer - 0x400000

        table_ldrxn1 = self.bit_mask_finder.pick_long(pointer)

        table_ldrxn2 = table_ldrxn1 + 16 * 2
        return ldx_instruction, table_ldrxn1, table_ldrxn2

    '''
    Get Values
    '''

    def getValues(self):
        try:
            ldx_instruction, table_ldrxn1, table_ldrxn2 = self.get_variant1()
        except ValueError:
            ldx_instruction, table_ldrxn1, table_ldrxn2 = self.get_variant2()

        # Return a dictionary of values, with the keys "PATCHADDR_LDRXN", "TABLE_LDRXN1", and "TABLE_LDRXN2"
        # mapped to the hexadecimal representations of the calculated addresses.
        return {
            "PATCHADDR_LDRXN": hex(ldx_instruction),
            "TABLE_LDRXN1": hex(table_ldrxn1),
            "TABLE_LDRXN2": hex(table_ldrxn2)
        }
