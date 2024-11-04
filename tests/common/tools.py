import threading
import time

from src.common import tools


class MockSingleton(metaclass=tools.SingletonMeta): ...


class MockFlyweight(metaclass=tools.FlyweightMeta):
    __slots__ = ("value",)

    def __init__(self, value: int) -> None:
        self.value = value


def test_singleton() -> None:
    inst1 = MockSingleton()
    inst2 = MockSingleton()
    assert inst1 is inst2


def test_flyweight_same_state() -> None:
    inst1 = MockFlyweight(1)
    inst2 = MockFlyweight(1)
    assert inst1 is inst2


def test_flyweight_diff_state() -> None:
    inst1 = MockFlyweight(1)
    inst2 = MockFlyweight(2)
    assert inst1 is not inst2


def test_unique_id_generator_single_thread() -> None:
    id1 = tools.generate_unique_id()
    id2 = tools.generate_unique_id()
    assert id1 != id2


def test_unique_id_generator_multi_threaded() -> None:
    ids: list[int] = []

    def generate_id() -> None:
        time.sleep(0.01)
        ids.append(tools.generate_unique_id())

    threads: list[threading.Thread] = []
    for _ in range(1_000):
        thread = threading.Thread(target=generate_id)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def test_camel_to_snake() -> None:
    assert tools.camel_case_to_snake_case("hello") == "hello"
    assert tools.camel_case_to_snake_case("Hello") == "hello"
    assert tools.camel_case_to_snake_case("HelloHello") == "hello_hello"
