import pytest

from exercise_6 import *


def test_safe_dict():
    sd = SafeDict({"a": 1, "b": 2, "nested": {"x": 10, "y": 20}})

    # Тесты на обычные ключи
    assert sd["a"] == 1
    assert sd["b"] == 2
    assert sd["c"] == "Key not found"

    # Тесты на вложенные словари
    nested_sd = sd["nested"]
    assert nested_sd["x"] == 10
    assert nested_sd["z"] == "Key not found"

    # Тесты на список ключей
    assert sd[["a", "b", "c"]] == [1, 2, "Key not found"]

    # Тесты на безопасное обновление
    sd.update("a", 100)
    assert sd["a"] == 100
    sd.update("c", 200)  # Key 'c' не существует

    # Тесты на безопасное удаление
    del sd["b"]
    assert sd["b"] == "Key not found"
    del sd["c"]  # Key 'c' не существует


def test_temp_env_var():
    with TempEnvVar("TEST_VAR", "123"):
        assert os.getenv("TEST_VAR") == "123"
    assert os.getenv("TEST_VAR") is None


def test_find_max_in_collections():
    collections = {
        "list": [5, 2, 9, 1, 5, 6],
        "tuple": (8, 4, 7, 3, 2, 6),
        "set": {10, 20, 5, 3},
        "dict": {"a": 1, "b": 22, "c": 15},
        "nested_list": [[1, 2], [3, 4, 5], [6]],
        "nested_tuple": ((1, 2), (3, 4, 5), (6,)),
        "custom1": CustomCollection([4, 9, 1]),
        "custom2": CustomCollection([2, 5, 3]),
        "mixed": [CustomCollection([1, 2]), (3, 4, 5), [6]],
    }

    expected = {
        "list": 9,
        "tuple": 8,
        "set": 20,
        "dict": 22,
        "nested_list": 6,
        "nested_tuple": 6,
        "custom1": 9,
        "custom2": 5,
        "mixed": 6,
    }

    max_values = find_max_in_collections(collections)

    for key, value in expected.items():
        assert (
            max_values[key] == value
        ), f"Expected {value} for {key}, but got {max_values[key]}"


def test_transpose_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose_matrix(matrix) == transposed


def test_annotated_function():
    assert annotated_function(5, "hello") is True
    assert annotated_function(5, 5) is False
    assert annotated_function("5", "hello") is False


# Тесты звуков животных
def test_animal_sounds():
    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)

    assert dog.sound() == "Woof"
    assert cat.sound() == "Meow"


# Тесты коммуникации между животными
def test_animal_communication():
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)
    cat1 = Cat("Whiskers", 2)
    cat2 = Cat("Mittens", 4)

    assert dog1.communicate(dog2) == "Buddy and Max bark together!"
    assert dog1.communicate(cat1) == "Buddy barks at Whiskers"
    assert cat1.communicate(dog1) == "Whiskers hisses at Buddy"
    assert cat1.communicate(cat2) == "Whiskers and Mittens purr together!"


# Тесты на некорректную реализацию
def test_not_implemented_error():
    with pytest.raises(TypeError):
        animal = BaseAnimal("Generic", 1)


# Тесты исключений (передача не животного)
def test_invalid_communication():
    dog = Dog("Buddy", 3)
    non_animal = "String object"

    with pytest.raises(AttributeError):
        dog.communicate(non_animal)


# Тестируем создание экземпляров с именем и возрастом
def test_animal_initialization():
    dog = Dog("Buddy", 3)
    assert dog.name == "Buddy"
    assert dog.age == 3
    cat = Cat("Whiskers", 2)
    assert cat.name == "Whiskers"
    assert cat.age == 2


def test_custom_collection_initialization():
    collection = CustomCollection([1, 2, 3])
    assert len(collection) == 3
    assert bool(collection) is True

    empty_collection = CustomCollection([])
    assert len(empty_collection) == 0
    assert bool(empty_collection) is False

    with pytest.raises(TypeError):
        CustomCollection("not a list")


def test_custom_collection_add():
    collection = CustomCollection([1])
    collection.add(2)
    assert len(collection) == 2
    assert collection.items == [1, 2]


def test_custom_collection_remove():
    collection = CustomCollection([1, 2, 3])
    collection.remove(2)
    assert len(collection) == 2
    assert collection.items == [1, 3]

    with pytest.raises(ValueError):
        collection.remove(4)  # Item not in collection


def test_custom_collection_find():
    collection = CustomCollection([1, 2, 3, 4])
    result = collection.find(lambda x: x > 2)
    assert result == 3

    result = collection.find(lambda x: x > 5)
    assert result is None


def test_custom_collection_clear():
    collection = CustomCollection([1, 2, 3])
    collection.clear()
    assert len(collection) == 0
    assert bool(collection) is False
