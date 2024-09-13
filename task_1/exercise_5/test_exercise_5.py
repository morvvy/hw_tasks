from exercise_5 import *


def test_resource_manager():
    resource_file = "resource.txt"
    with ResourceManager() as r:
        r.write("Resource in use\n")

    with open(resource_file, "r") as rf:
        content = rf.read()

    assert "Resource initialized" in content
    assert "Resource in use" in content
    assert "Resource released" in content


def test_check_nested_mutability():
    lst = [[1, 2], [3, 4]]
    result = check_nested_mutability(lst)
    assert result[0][0] == "modified"

    tpl = ([1, 2], (3, 4))
    result = check_nested_mutability(tpl)
    assert result[0][0] == "modified"

    try:
        check_nested_mutability({1: "a"})
    except TypeError as e:
        assert str(e) == "Unsupported data type"


def test_create_matrix():
    assert create_matrix(2, 3) == [[0, 1, 2], [3, 4, 5]]
    assert create_matrix(3, 3) == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def test_fibonacci():
    gen = fibonacci()
    result = [next(gen) for _ in range(10)]
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_advanced_function():
    assert advanced_function(1, 2, 3, sum_a=4, concat_b="hello", sum_c=10) == (
        20,
        "hello",
    )
    assert advanced_function(1.5, 2.5, "abc", concat_name="def", sum_val=5) == (
        9.0,
        "abcdef",
    )
    assert advanced_function(100, concat_a="A", concat_b="B", sum_x=50) == (150, "AB")
    assert advanced_function() == (0, "")


def test_polymorphism():
    vehicles = [Car(fuel=50), Bike(), ElectricScooter(battery_level=100)]

    # Тестирование разных транспортных средств
    assert vehicles[0].drive() == "Driving a car at 60 km/h, remaining fuel: 40"
    assert vehicles[1].drive() == "Riding a bike at 20 km/h"
    assert (
        vehicles[2].drive() == "Riding an electric scooter with 80% battery remaining"
    )

    # Фабричный метод
    factory = VehicleFactory()
    vehicle = factory.create_vehicle("car", fuel=30)
    assert vehicle.drive() == "Driving a car at 60 km/h, remaining fuel: 20"
    vehicle.refuel(10)
    assert vehicle.fuel == 30

    # Проверка исключений
    try:
        empty_scooter = factory.create_vehicle("electric_scooter", battery_level=0)
        empty_scooter.drive()
    except ValueError as e:
        assert str(e) == "Battery empty!"
