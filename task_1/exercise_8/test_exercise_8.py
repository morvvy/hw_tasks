import pytest

from exercise_8 import *


# Тест для подключения и отключения от базы данных
def test_database_connection():
    db = DatabaseConnection("test_db")
    with db:
        assert db.connection == "Connected to test_db database"
    assert db.connection is None


# Тест для выполнения SQL-запросов
def test_execute_query():
    db = DatabaseConnection("test_db")
    with db:
        db.start_transaction()
        result = db.execute_query("SELECT * FROM users")
        assert result == "Result of 'SELECT * FROM users'"
        assert db.transaction_active is True
        db.commit()
        assert db.transaction_active is False


# Тест для отката транзакции при возникновении ошибки
def test_rollback_on_exception():
    db = DatabaseConnection("test_db")
    with pytest.raises(RuntimeError, match="Test exception"):
        with db:
            db.start_transaction()
            assert db.transaction_active is True
            raise RuntimeError("Test exception")
    assert db.transaction_active is False
    assert db.connection is None


# Тест для ошибки при выполнении запроса без транзакции
def test_execute_query_without_transaction():
    db = DatabaseConnection("test_db")
    with db:
        with pytest.raises(RuntimeError, match="No active transaction"):
            db.execute_query("SELECT * FROM users")


# Тест для ошибки при коммите без активной транзакции
def test_commit_without_transaction():
    db = DatabaseConnection("test_db")
    with db:
        with pytest.raises(RuntimeError, match="No active transaction to commit"):
            db.commit()


# Тест для отложенного подключения (без вызова connect)
def test_lazy_connection():
    db = DatabaseConnection("test_db")
    assert db.connection is None
    with db:
        assert db.connection == "Connected to test_db database"


def test_enumerate_list():
    # Базовые тесты
    assert enumerate_list(["a", "b", "c"]) == [(0, "a"), (1, "b"), (2, "c")]
    assert enumerate_list([10, 20, 30]) == [(0, 10), (1, 20), (2, 30)]

    # Тест с кастомным стартовым индексом
    assert enumerate_list(["a", "b", "c"], start=1) == [(1, "a"), (2, "b"), (3, "c")]

    # Тест с кастомным шагом
    assert enumerate_list(["x", "y", "z"], step=2) == [(0, "x"), (2, "y"), (4, "z")]

    # Тест с кастомным стартом и шагом
    assert enumerate_list([100, 200, 300], start=10, step=5) == [
        (10, 100),
        (15, 200),
        (20, 300),
    ]


def test_all_unique_elements():
    assert all_unique_elements([1, 2, 3, 4, 5]) is True
    assert all_unique_elements([1, 2, 2, 3, 4]) is False
    assert all_unique_elements([]) is True
    assert all_unique_elements([None, None, 1, 2, 3]) is True
    assert (
        all_unique_elements("abcde") is True
    )  # Теперь строки обрабатываются корректно
    assert all_unique_elements([(1, 2), (3, 4), (1, 2)]) is False
    assert (
        all_unique_elements([{"key1": 1, "key2": 2}, {"key1": 1, "key2": 2}]) is False
    )
    assert all_unique_elements([1, "1", 1.0]) is False


def test_analyze_even_numbers():
    assert analyze_even_numbers([1, 2, 3, 4, 5]) == {
        "count": 2,
        "sum": 6,
        "average": 3.0,
        "max": 4,
        "min": 2,
    }, "Test case 1 failed"

    assert analyze_even_numbers([2, 4, 6, 8, 10]) == {
        "count": 5,
        "sum": 30,
        "average": 6.0,
        "max": 10,
        "min": 2,
    }, "Test case 2 failed"

    assert analyze_even_numbers([1, 3, 5, 7, 9]) == {
        "count": 0,
        "sum": None,
        "average": None,
        "max": None,
        "min": None,
    }, "Test case 3 failed"

    assert analyze_even_numbers([]) == {
        "count": 0,
        "sum": None,
        "average": None,
        "max": None,
        "min": None,
    }, "Test case 4 failed"

    assert analyze_even_numbers([-2, -4, -6, 8, 10]) == {
        "count": 5,
        "sum": 6,
        "average": 1.2,
        "max": 10,
        "min": -6,
    }, "Test case 5 failed"

    assert analyze_even_numbers([1, 3, 5, 7, 9, 10**6]) == {
        "count": 1,
        "sum": 1000000,
        "average": 1000000.0,
        "max": 1000000,
        "min": 1000000,
    }, "Test case 6 failed"


def test_count_unique_words():
    # Тест с разным регистром
    assert count_unique_words("Hello world hello") == 2
    # Тест с пунктуацией
    assert count_unique_words("One, two. Three? Two; one!") == 3
    # Тест с пустым текстом
    assert count_unique_words("") == 0
    # Тест с одними и теми же словами
    assert count_unique_words("word word word") == 1
    # Тест с текстом без повторений
    assert count_unique_words("A quick brown fox jumps over the lazy dog") == 9
    # Тест с пробелами
    assert count_unique_words("   ") == 0


class Example:
    def __init__(self):
        self.value = 42
        self.another_value = 99


def test_multi_temp_attributes():
    example = Example()

    # Проверка изменения нескольких атрибутов
    with MultiTempAttributes(example, {"value": 100, "another_value": 200}):
        assert example.value == 100
        assert example.another_value == 200

    assert example.value == 42
    assert example.another_value == 99
