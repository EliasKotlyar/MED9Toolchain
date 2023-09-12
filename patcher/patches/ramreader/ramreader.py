from patcher.src.abstract_patch import AbstractPatch


class RamReader(AbstractPatch):

    def patch_kwp_table(self, offset, sid, funcname):
        # Set 20 bytes with "00"
        self.file.write_bytes(hex(offset), "00" * 20)
        # Set SID:
        self.file.write_byte(hex(offset), sid)
        self.file.write_bytes(hex(offset + 1), "FF" * 3)
        # Set "KWP Flag" - can be 3F , 3C or 10 or 38. Depending on Service. 38 works mostly.
        self.file.write_byte(hex(offset + 7), 0x38)
        # Set Func Address:
        func_addr = int(self.file.get_memorymap(funcname), 16)
        func_addr = func_addr - 0x400000
        self.file.write_long(hex(offset + 8), func_addr)
        pass

    def patch_read_memory(self):
        kwp_table_address = int(self.file.get_analysis("KWP_TABLE"), 16)
        self.patch_kwp_table(kwp_table_address, 0x23, "FUNC_READMEMORYBYADDRESS")
        pass

    def patch_write_memory(self):
        kwp_table_address = int(self.file.get_analysis("KWP_TABLE"), 16)
        kwp_table_address += 20
        self.patch_kwp_table(kwp_table_address, 0x3D, "FUNC_WRITEMEMORYBYADDRESS")
        pass

    def apply_patch(self):
        self.patch_write_memory()
        self.patch_read_memory()
        pass

    def get_info(self):
        return "Patches RAMREADER"
        pass

    def get_name(self):
        return "ramreader"

    def get_c_files(self):
        return ["ramreader.c", "ramwriter.c", "ramreader.h"]
