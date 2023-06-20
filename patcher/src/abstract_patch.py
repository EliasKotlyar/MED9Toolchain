from patcher.src.patch_file import PatchFile


class AbstractPatch:
    def __init__(self):
        self.file = None
        return

    def patch(self):
        raise NotImplementedError("Subclasses must implement the patch method.")

    def get_info(self):
        raise NotImplementedError("Subclasses must implement the get_info method.")

    def get_name(self):
        raise NotImplementedError("Subclasses must implement the get_name method.")

    def get_c_files(self):
        raise NotImplementedError("Subclasses must implement the get_c_files method.")

    def setFile(self, file: PatchFile):
        self.file = file
        return
