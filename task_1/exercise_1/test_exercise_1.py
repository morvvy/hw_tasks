import pytest

from exercise_1 import *


def test_modify_nested_data():
    data = [1, 2, [3, 4, {"a": 5, "b": [6, 7], "c": (8, 9)}], (10, 11)]
    result = modify_nested_data(data)
    assert result == [
        1,
        2,
        [
            3,
            4,
            {"a": 5, "b": [6, 7, "modified"], "c": (8, 9), "new_key": "new_value"},
            "modified",
        ],
        (10, 11),
        "modified",
    ]

    data = {"key1": "value1", "key2": [1, 2, {3, 4}], "key3": (5, 6)}
    result = modify_nested_data(data)
    assert result == {
        "key1": "value1",
        "key2": [1, 2, {3, 4, "new_element"}, "modified"],
        "key3": (5, 6),
        "new_key": "new_value",
    }

    data = []
    result = modify_nested_data(data)
    assert result == ["modified"]

    data = {}
    result = modify_nested_data(data)
    assert result == {"new_key": "new_value"}

    data = set()
    result = modify_nested_data(data)
    assert result == {"new_element"}

    data = (1, 2, 3)
    result = modify_nested_data(data)
    assert result == (1, 2, 3)

    data = 123
    result = modify_nested_data(data)
    assert result == 123

    data = "immutable"
    result = modify_nested_data(data)
    assert result == "immutable"


def test_reverse_with_depth():

    lst = [1, 2, 3]
    tpl = (1, 2, 3)
    result_lst, result_tpl = reverse_with_depth(lst, tpl, 1)
    assert result_lst == [3, 2, 1]
    assert result_tpl == (3, 2, 1)

    lst = [1, [2, 3], 4]
    tpl = (1, (2, 3), 4)
    result_lst, result_tpl = reverse_with_depth(lst, tpl, 2)
    assert result_lst == [4, [3, 2], 1]
    assert result_tpl == (4, (3, 2), 1)

    lst = [1, [2, 3], 4]
    tpl = (1, (2, 3), 4)
    result_lst, result_tpl = reverse_with_depth(lst, tpl, 1)
    assert result_lst == [4, [2, 3], 1]
    assert result_tpl == (4, (2, 3), 1)

    lst = [1, [2, 3], 4]
    tpl = (1, (2, 3), 4)
    result_lst, result_tpl = reverse_with_depth(lst, tpl, 0)
    assert result_lst == [1, [2, 3], 4]
    assert result_tpl == (1, (2, 3), 4)

    lst = [1, "a", [2, 3], "b"]
    tpl = (1, "a", (2, 3), "b")
    result_lst, result_tpl = reverse_with_depth(lst, tpl, 2)
    assert result_lst == ["b", [3, 2], "a", 1]
    assert result_tpl == ("b", (3, 2), "a", 1)

    lst = []
    tpl = ()
    result_lst, result_tpl = reverse_with_depth(lst, tpl, 1)
    assert result_lst == []
    assert result_tpl == ()


def test_pairwise_operations():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    result = pairwise_operations(lst1, lst2, operation=lambda x, y: x + y)
    expected = [(0, 5), (1, 7), (2, 9)]
    assert result == expected


def test_modify_external_state():
    lst = [1, 2, 3]
    modify_external_state(lst)
    assert lst == [1, 2, 3, "modified"]


def test_compute_difference():
    result = compute_difference(10, 3)
    assert result == 7


def test_infinite_sequence():
    gen = infinite_sequence(5, limit=10)
    result = list(gen)
    expected = [5, 6, 7, 8, 9, 10]
    assert result == expected


def test_flexible_function():
    result = flexible_function(1, 2, 3, x=2, y=3, z=4)
    assert result == (6, 24)
