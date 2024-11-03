import logging
import os
import typing

from src.tools import func


def get_file_handler(name: str) -> logging.FileHandler:
    logs_dir = func.get_root_folder() / "logs"
    os.makedirs(logs_dir, exist_ok=True)

    file = logging.FileHandler(
        filename=logs_dir / f"{name}.log",
        encoding="utf-8",
        mode="a",
    )
    file.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(name)s %(levelname)s -> %(message)s",
            datefmt="%Y.%m.%d %H:%M",
        )
    )

    return file


def get_stream_handler(name: str) -> logging.StreamHandler[typing.Any]:
    stream = logging.StreamHandler()
    stream.setFormatter(logging.Formatter(fmt="%(levelname)s %(name)s -> %(message)s", datefmt="%Y.%m.%d %H:%M"))
    return stream
