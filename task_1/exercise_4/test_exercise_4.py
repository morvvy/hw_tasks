from exercise_4 import *


def test_copy_comparison():
    shallow_copy, deep_copy = copy_comparison()
    assert shallow_copy[0][0] == 99
    assert deep_copy[0][0] == 1


def test_modify_elements():
    lst, tpl, tuple_error = modify_elements()
    assert lst == [99, 2, 3]
    assert tpl == (1, 2, 3)
    assert "does not support item assignment" in tuple_error


def test_create_tuples():
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    assert create_tuples(list1, list2) == [(0, 1, "a"), (1, 2, "b"), (2, 3, "c")]

    list1 = [1, 2]
    list2 = ["x", "y", "z"]
    assert create_tuples(list1, list2) == [(0, 1, "x"), (1, 2, "y")]


def test_factorial_functions():
    assert factorial(5) == 120
    assert list(factorial_generator(5)) == [2, 6, 24, 120]
    assert factorial(0) == 1
    assert list(factorial_generator(0)) == []


def test_classify_package():
    assert classify_package("numpy") == "library"
    assert classify_package("django") == "framework"
    assert classify_package("math") == "module"
    assert classify_package("nonexistent") == "unknown"


def test_worker_polymorphism():
    workers = [Programmer(), Designer()]
    assert workers[0].do_work() == "Writing code"
    assert workers[1].do_work() == "Designing interface"


def test_private_account():
    account = PrivateAccount(100)
    assert account.get_balance() == 100
    account.deposit(50)
    assert account.get_balance() == 150
    account.deposit(-50)
    assert account.get_balance() == 150
