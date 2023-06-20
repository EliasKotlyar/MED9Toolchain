from patcher.src.abstract_patch import AbstractPatch


class MapSwitch(AbstractPatch):
    def apply_patch(self):
        patchAddr = self.file.get_analysis("PATCHADDR_LDRXN")
        funcAddr = self.file.get_memorymap("FUNC_GET_LDRXN_ADR")
        list = [
            "bl " + funcAddr,
        ]
        code = self.file.assemble(list)
        self.file.write_bytes(patchAddr, code)
        pass

    def get_info(self):
        return "Patches a small Mapswitch (LDRXN)"
        pass

    def get_name(self):
        return "mapswitch_ldrxn"

    def get_c_files(self):
        return ["mapswitch.c"]
