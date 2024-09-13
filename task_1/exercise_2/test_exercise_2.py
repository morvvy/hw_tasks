from exercise_2 import *


def test_sum_indexed_elements():
    assert sum_indexed_elements([1, 2, 3]) == [1, 3, 5]
    assert sum_indexed_elements([0, 0, 0]) == [0, 1, 2]


def test_pairwise_sums():
    assert pairwise_sums([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert pairwise_sums([1, 2], [3, 4, 5]) == [4, 6]


def test_simple_procedure(capsys):
    simple_procedure()
    captured = capsys.readouterr()
    assert captured.out == "This is a procedure\n"


def test_simple_function():
    assert simple_function() == "This is a function"


def test_simple_generator():
    gen = simple_generator()
    assert next(gen) == "This is"
    assert next(gen) == "a generator"


def test_count_arguments():
    assert count_arguments(1, 2, 3, a=4, b=5) == 5
    assert count_arguments("a", "b") == 2
    assert count_arguments() == 0
    assert count_arguments(x=1, y=2, z=3) == 3


def test_bank_account():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100
    account.withdraw(50)
    assert account.get_balance() == 50
    account.withdraw(100)
    assert account.get_balance() == 50


def test_vector_operations():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    assert v1 + v2 == Vector(4, 6)
    assert repr(v1) == "Vector(1, 2)"
    assert v1 == Vector(1, 2)
    assert v1 != Vector(2, 3)


def test_file_manager(tmp_path):
    test_file = tmp_path / "test_file.txt"
    with FilesManager(test_file, "w") as f:
        f.write("Hello, world!")

    with FilesManager(test_file, "r") as f:
        content = f.read()

    assert content == "Hello, world!"
