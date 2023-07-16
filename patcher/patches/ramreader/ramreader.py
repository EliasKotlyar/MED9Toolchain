from patcher.src.abstract_patch import AbstractPatch


class MapSwitch(AbstractPatch):
    def get_func(self, funcname):
        funcAddr = int(self.file.get_memorymap(funcname), 16)
        funcAddr = funcAddr - 0x400000
        return funcAddr

    def patch_read_memory(self):
        kwp_table_address = int(self.file.get_analysis("KWP_TABLE"), 16)
        # Patch the service-id:
        self.file.write_byte(hex(kwp_table_address), 0x23)
        # Patch the Function Address:
        self.file.write_long(hex(kwp_table_address + 8), self.get_func("FUNC_READMEMORYBYADDRESS"))
        pass

    def patch_write_memory(self):
        kwp_table_address = int(self.file.get_analysis("KWP_TABLE"), 16)
        kwp_table_address += 20
        # Patch the service-id:
        self.file.write_byte(hex(kwp_table_address), 0x3D)
        # Patch the Function Address:
        self.file.write_long(hex(kwp_table_address + 8), self.get_func("FUNC_WRITEMEMORYBYADDRESS"))
        pass

    def apply_patch(self):
        pass

    def get_info(self):
        return "Patches RAMREADER"
        pass

    def get_name(self):
        return "ramreader"

    def get_c_files(self):
        return ["ramreader.c", "ramwriter.c"]
