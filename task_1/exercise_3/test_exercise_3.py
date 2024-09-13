from exercise_3 import *


def test_lists_to_dict():
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    assert lists_to_dict(keys, values) == {"a": 1, "b": 2, "c": 3}

    keys = [1, 2, 3]
    values = ["x", "y", "z"]
    assert lists_to_dict(keys, values) == {1: "x", 2: "y", 3: "z"}

    keys = []
    values = []
    assert lists_to_dict(keys, values) == {}


def test_generate_numbers():
    gen = generate_numbers(5)
    assert list(gen) == [0, 1, 2, 3, 4]


def test_sum_generator():
    gen = generate_numbers(5)
    assert sum_generator(gen) == 10


def test_serialize_generator():
    gen = generate_numbers(5)
    assert serialize_generator(gen) == "[0, 1, 2, 3, 4]"


def test_validate_param_types():
    assert validate_param_types(1, 1.5, "test") is True
    assert validate_param_types(1, "1.5", "test") is False
    assert validate_param_types("1", 1.5, "test") is False
    assert validate_param_types(1, 1.5, 2) is False


def test_shape_area():
    rect = Rectangle(4, 5)
    circle = Circle(3)

    assert rect.area() == 20
    assert round(circle.area(), 2) == 28.27


def test_private_data():
    private_data = PrivateData("secret")
    assert private_data.get_data() == "secret"


def test_complex_number_operations():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    assert c1 + c2 == ComplexNumber(4, 6)
    assert repr(c1) == "(1 + 2i)"
    assert c1 == ComplexNumber(1, 2)
    assert c1 != ComplexNumber(2, 3)


def test_long_operation_manager(capsys):
    import time

    with LongOperationManager():
        time.sleep(1)

    captured = capsys.readouterr()
    assert "Start long operation" in captured.out
    assert "End long operation in" in captured.out
