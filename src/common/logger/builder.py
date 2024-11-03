import logging
import typing

from src.common import interfaces

from . import utils


class LoggerBuilder(interfaces.BuilderType[logging.Logger]):
    __slots__ = ("_logger",)

    def __init__(self, name: str, level: int = logging.WARN) -> None:
        self._logger = logging.Logger(name, level=level)

    def set_file_handler(self, level: int = logging.WARN) -> typing.Self:
        handler = utils.get_file_handler(self._logger.name)
        handler.setLevel(level)
        return self.set_handler(handler)

    def set_stream_handler(self, level: int = logging.INFO) -> typing.Self:
        handler = utils.get_stream_handler(self._logger.name)
        handler.setLevel(level)
        return self.set_handler(handler)

    def set_handler(self, handler: logging.Handler) -> typing.Self:
        self._logger.addHandler(handler)
        return self

    def build(self) -> logging.Logger:
        return self._logger
