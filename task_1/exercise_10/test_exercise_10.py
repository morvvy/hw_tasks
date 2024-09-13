import os
import time

import pytest

from exercise_10 import *


def test_binary_search():
    sorted_list = list(range(1000000))
    target = 999999

    start_time = time.time()
    result = search_with_validation(sorted_list, target)
    assert result == 999999
    assert time.time() - start_time < 1


def test_search_with_unsorted_list():
    unsorted_list = [3, 1, 4, 1, 5, 9]

    try:
        search_with_validation(unsorted_list, 1)
    except ValueError as e:
        assert str(e) == "List must be sorted"


def test_cache_and_retry():
    calls = []

    @cache_and_retry(retries=3, delay=0.1)
    def unreliable_function(x):
        if len(calls) < 2:
            calls.append(x)
            raise ValueError("Temporary error")
        return x * 2

    # Первая попытка должна завершиться неудачей, вторая должна сработать
    assert unreliable_function(3) == 6
    assert unreliable_function(3) == 6  # Из кэша
    assert len(calls) == 2  # Функция была вызвана 2 раза


def test_create_incrementer():
    incr = create_incrementer(10)

    assert incr() == 11
    assert incr() == 12
    incr("increment", 5)
    assert incr() == 18
    incr("reset")
    assert incr() == 5


@pytest.mark.asyncio
async def test_run_tasks():
    task_list = [1, 2, 3, 4]
    results = await run_tasks(task_list)

    assert results == [
        "Task 1 failed",
        "Task 2 completed",
        "Task 3 failed",
        "Task 4 completed",
    ]


def test_complex_number_comparison():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    assert str(c1 + c2) == "4 + 6i"
    assert str(c1 * c2) == "-5 + 10i"
    assert abs(c1) == (1**2 + 2**2) ** 0.5
    assert c1 < c2
    assert c1 != c2


def test_write_to_file_with_logging():
    filename = "test.txt"
    content = "Hello, world!"
    log_filename = "test_log.txt"

    write_to_file_with_logging(filename, content)

    with open(filename, "r") as f:
        assert f.read() == content

    # Пытаемся вызвать ошибку для записи в лог
    try:
        with FileManagerWithLogging(filename, "x", log_filename) as f:
            pass
    except FileExistsError:
        pass

    with open(os.path.join(os.getcwd(), log_filename), "r") as log_file:
        assert "FileExistsError" in log_file.read()
