import time
from unittest.mock import mock_open, patch

import pytest

from exercise_9 import *


def test_list_tuple_operations_deep():
    lst = [1, [2, 3], [4, [5, 6]]]
    tpl = (1, (2, 3), (4, (5, 6)))

    updated_lst, error_msg, list_time, tuple_time = list_tuple_operations_deep(lst, tpl)

    assert updated_lst == [
        "modified",
        ["modified", "modified"],
        ["modified", ["modified", "modified"]],
    ]
    assert "does not support item assignment" in error_msg
    assert list_time > 0
    assert tuple_time > 0


def test_square_numbers():
    # Тестирование правильности результата функции square_numbers
    assert square_numbers(5) == [1, 4, 9, 16, 25]
    assert square_numbers(0) == []
    assert square_numbers(1) == [1]
    assert square_numbers(3) == [1, 4, 9]


def test_square_numbers_generator():
    # Тестирование правильности результата генератора
    assert list(square_numbers_generator(5)) == [1, 4, 9, 16, 25]
    assert list(square_numbers_generator(0)) == []
    assert list(square_numbers_generator(1)) == [1]
    assert list(square_numbers_generator(3)) == [1, 4, 9]


def test_memory_usage_comparison():
    # Тестирование сравнения использования памяти между списком и генератором
    tracemalloc.start()
    list_memory, gen_memory = memory_usage_comparison(1000)
    tracemalloc.stop()

    # Проверяем, что память, используемая списком, больше, чем память, используемая генератором
    assert list_memory > gen_memory


def test_my_container():
    c = MyContainer([1, 2, 3])
    assert len(c) == 3
    assert str(c) == "MyContainer with 3 items"
    assert c[1] == 2


@patch("builtins.open", new_callable=mock_open)
def test_file_open_and_close(mock_file):
    filename = "test.txt"
    mode = "r"

    with FileManager(filename, mode) as f:
        # Verify that the file was opened with correct parameters
        mock_file.assert_called_once_with(filename, mode)
        assert f == mock_file()

    # Verify that the file was closed after exiting the 'with' block
    mock_file().close.assert_called_once()


@patch("builtins.open", new_callable=mock_open)
def test_file_open_exception(mock_file):
    filename = "test.txt"
    mode = "r"

    # Create a scenario where an exception occurs inside the 'with' block
    with pytest.raises(ValueError, match="An error occurred"):
        with FileManager(filename, mode):
            raise ValueError("An error occurred")

    # Verify that the file was closed even if an exception is raised
    mock_file().close.assert_called_once()


@patch("builtins.open", new_callable=mock_open)
def test_file_write(mock_file):
    filename = "test.txt"
    mode = "w"

    with FileManager(filename, mode) as f:
        f.write("Test")

    # Verify that the file was opened in write mode
    mock_file.assert_called_once_with(filename, mode)

    # Verify that the write operation was performed
    mock_file().write.assert_called_once_with("Test")

    # Verify that the file was closed after exiting the 'with' block
    mock_file().close.assert_called_once()


@pytest.fixture
def dog():
    return Dog(name="Buddy", mood="neutral", hunger=5, tiredness=5)


@pytest.fixture
def cat():
    return Cat(name="Whiskers", mood="happy", hunger=8, tiredness=6)


@pytest.fixture
def ball():
    return Toy(name="ball", is_fun=True)


def test_initial_states(dog):
    assert dog.hunger == 5
    assert dog.tiredness == 5
    assert dog.mood == "neutral"


def test_feed(dog):
    dog.feed()
    assert dog.hunger == 2  # Голод уменьшен на 3


def test_rest(dog):
    dog.rest()
    assert dog.tiredness == 2  # Усталость уменьшена на 3


def test_play_changes_mood(dog, ball):
    dog.play(ball)
    assert dog.mood == "happy"
    assert dog.tiredness == 7  # Увеличена усталость


def test_speak_happy_dog(dog, ball):
    dog.play(ball)
    assert dog.speak() == "Woof! I'm happy!"


def test_speak_hungry_cat(cat):
    assert cat.speak() == "Meow! I'm hungry!"


def test_invalid_hunger_value():
    dog = Dog(name="Buddy", mood="neutral")
    with pytest.raises(ValueError):
        dog.hunger = 11  # Неверное значение голода
