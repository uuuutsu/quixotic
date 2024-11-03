import threading
import time

from src.common import tools


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
