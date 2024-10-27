from src.tools import cls


class MockSingleton(metaclass=cls.SingletonMeta): ...


class MockFlyweight(metaclass=cls.FlyweightMeta):
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
