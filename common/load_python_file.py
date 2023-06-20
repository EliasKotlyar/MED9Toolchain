import importlib
import os
import sys
import importlib.util


def load_python_file(filepath: str, sub_class_to_find: object) -> object:
    # Method for getting the class object from a file.
    # It takes the file path as input and returns the class object.
    module_name = os.path.basename(filepath)
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module

    for name, obj in module.__dict__.items():
        if isinstance(obj, type) and issubclass(obj, sub_class_to_find) and obj != sub_class_to_find:
            return obj
    return None


def get_python_file_from_obj(obj: object) -> str:
    cls = type(obj)
    module_name = cls.__module__
    module = sys.modules[module_name]
    filename = module.__file__
    return filename
