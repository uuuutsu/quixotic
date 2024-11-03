import pathlib


def get_root_folder() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent.parent.parent
