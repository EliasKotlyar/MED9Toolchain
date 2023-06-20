from analysis.addresses.abstract_addressprovider import AbstractAddressProvider


# This class represents the free memory addresses where the code can be patched.
# It extends the AbstractAddressProvider class.
class FreeMemory(AbstractAddressProvider):
    def align(self, current_address) -> int:
        # This method takes a current address and finds the next aligned address
        # that has a lot of zeros in its hexadecimal representation.
        target_address = current_address

        while True:
            target_address += 1
            target_address_str = hex(target_address)

            # Check if the target address has a lot of zeros at the end.
            if target_address_str.endswith('00'):
                break

        return int(target_address_str, 16)

    def getValues(self) -> []:
        # Calculate the addresses for free flash and free RAM memory.
        free_ram = 0x800000
        free_ram += 0xD000

        # Create a signature string for finding the free flash memory address.
        signature = "02 03 06 00 5A 5A 5A 5A"
        area_len = 0x10000
        signature += "FF" * area_len

        # Use the bit_mask_finder object to find the address based on the signature.
        sigAddress = self.bit_mask_finder.find_by_signature(signature)

        # Align the found address to the next address with a lot of zeros.
        free_flash = self.align(sigAddress)
        free_flash += 0x400000

        # Return a dictionary of values, with the keys "FREE_FLASH_MEMORY" and "FREE_RAM_MEMORY"
        # mapped to the hexadecimal representations of the calculated addresses.
        return {
            "FREE_FLASH_MEMORY": hex(free_flash),
            "FREE_RAM_MEMORY": hex(free_ram),
        }
