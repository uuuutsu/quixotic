import threading
import typing

from src.common import tools


@typing.final
class _Counter(metaclass=tools.SingletonMeta):
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._counter = 0

    def step(self) -> int:
        with self._lock:
            self._counter += 1
            return self._counter


_COUNTER: typing.Final[_Counter] = _Counter()


def generate_unique_id() -> int:
    return _COUNTER.step()
