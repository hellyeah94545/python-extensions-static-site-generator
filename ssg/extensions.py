import sys
import importlib
from pathlib import Path


def load_module(directory, name):
    """

    :param directory: location of file
    :param name: file name
    :return: module object
    """
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)

def load_directory(directory):
    """

    :param directory: Extention directory
    :return:
    """
    for path in directory.rglob("*.py"):
            load_module(directory.as_posix(), path.stem)
