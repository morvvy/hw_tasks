from exercise_7 import *


def test_execution_timer_basic():
    with ExecutionTimer() as timer:
        time.sleep(1)
    assert (
        1 <= timer.execution_time < 1.1
    ), "Execution time should be close to 1 second."


def test_execution_timer_exception_handling():
    with ExecutionTimer() as timer:
        try:
            raise ValueError("Test error")
        except ValueError:
            pass
    assert (
        timer.execution_time >= 0
    ), "Execution time should be recorded even with exception."


def test_execution_timer_multiple_runs():
    timer = ExecutionTimer()
    with timer:
        time.sleep(0.5)
    with timer:
        time.sleep(0.7)
    avg_time = timer.average_execution_time()
    assert (
        0.5 <= avg_time < 0.8
    ), "Average execution time should be between 0.5 and 0.8 seconds."


def test_execution_timer_cpu_time():
    timer = ExecutionTimer(use_cpu_time=True)
    with timer:
        for _ in range(1000000):
            pass
    assert timer.execution_time >= 0, "CPU execution time should be recorded."


def test_find_common_elements_recursive():
    # Тест 1: Простое пересечение множеств
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    assert find_common_elements_recursive(set_a, set_b) == {3, 4}

    # Тест 2: Пересечение строк
    set_a = {"a", "b", "c"}
    set_b = {"c", "d", "e"}
    assert find_common_elements_recursive(set_a, set_b) == {"c"}

    # Тест 3: Несколько множеств без пересечений
    set_a = {1, 2, 3}
    set_b = {4, 5, 6}
    assert find_common_elements_recursive(set_a, set_b) == set()

    # Тест 4: Пересечение нескольких множеств
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5}
    set_c = {4, 5, 6}
    assert find_common_elements_recursive(set_a, set_b, set_c) == {4}

    # Тест 5: Пересечение с вложенными множествами
    set_a = {1, 2, frozenset({3, 4})}
    set_b = {frozenset({3, 4}), 5, 6}
    assert find_common_elements_recursive(set_a, set_b) == {frozenset({3, 4})}

    # Тест 6: Пересечение с вложенными кортежами
    set_a = {1, 2, (3, 4)}
    set_b = {(3, 4), 5, 6}
    assert find_common_elements_recursive(set_a, set_b) == {(3, 4)}

    # Тест 7: Смешанные типы данных
    set_a = {1, "abc", frozenset({3, 4})}
    set_b = {"abc", frozenset({3, 4}), 5}
    assert find_common_elements_recursive(set_a, set_b) == {"abc", frozenset({3, 4})}

    # Тест 8: Пустые множества
    set_a = {1, 2, 3}
    set_b = set()
    assert find_common_elements_recursive(set_a, set_b) == set()

    # Тест 9: Ошибка при передаче не множеств
    try:
        find_common_elements_recursive(set_a, [1, 2, 3])
    except ValueError as e:
        assert str(e) == "Все аргументы должны быть множествами."
    else:
        assert False, "Ожидалось исключение ValueError"


def test_lists_to_dict():
    # Пример с одинаковым количеством ключей и значений
    keys = ["name", "age", "city"]
    values = ["Alice", 25, "New York"]
    assert lists_to_dict(keys, values) == {
        "name": "Alice",
        "age": 25,
        "city": "New York",
    }

    # Пример с разным количеством ключей и значений (больше ключей)
    keys = ["x", "y", "z"]
    values = [10, 20]
    assert lists_to_dict(keys, values) == {"x": 10, "y": 20, "z": None}

    # Пример с разным количеством ключей и значений (больше значений)
    keys = ["a", "b"]
    values = [1, 2, 3]
    assert lists_to_dict(keys, values) == {"a": 1, "b": 2}

    # Пример с пустыми списками
    keys = []
    values = []
    assert lists_to_dict(keys, values) == {}

    # Пример с ключами или значениями содержащими None
    keys = ["key1", None, "key3"]
    values = [1, 2]
    assert lists_to_dict(keys, values) == {"key1": 1, None: 2, "key3": None}

    # Пример с ключами и значениями разного типа
    keys = ["a", "b", "c"]
    values = [1, "two", 3.0]
    assert lists_to_dict(keys, values) == {"a": 1, "b": "two", "c": 3.0}


def test_combine_strings():
    assert combine_strings(["Hello", "World"]) == "HelloWorld"
    assert combine_strings(["Hello", "World"], delimiter=" ") == "Hello World"
    assert combine_strings(["Hello", "World"], transform_func=str.upper) == "HELLOWORLD"
    assert (
        combine_strings(["Hello", "World"], transform_func=str.upper, delimiter="-")
        == "HELLO-WORLD"
    )

    try:
        combine_strings(["Hello", 1])  # Should raise ValueError
    except ValueError:
        pass

    try:
        combine_strings(
            ["Hello", "World"], transform_func="not_a_function"
        )  # Should raise ValueError
    except ValueError:
        pass


def test_media_play():
    # Тестирование общего поведения
    media_files = [
        Music(title="Song A", duration="3:45", genre="Rock"),
        Video(title="Movie B", duration="2:30:00", resolution="1080p"),
    ]

    assert media_files[0].play() == "Playing music: Song A in genre Rock"
    assert media_files[1].play() == "Playing video: Movie B at resolution 1080p"

    assert media_files[0].pause() == "Paused Song A"
    assert media_files[1].pause() == "Paused Movie B"

    assert media_files[0].pause() == "Song A is not playing"
    assert media_files[1].pause() == "Movie B is not playing"

    assert media_files[0].get_info() == "Title: Song A, Duration: 3:45"
    assert media_files[1].get_info() == "Title: Movie B, Duration: 2:30:00"

    # Проверка состояния воспроизведения
    assert media_files[0].play() == "Playing music: Song A in genre Rock"
    assert media_files[1].play() == "Playing video: Movie B at resolution 1080p"

    assert media_files[0].play() == "Song A (Music) is already playing"
    assert media_files[1].play() == "Movie B (Video) is already playing"


def test_custom_stack():
    stack = CustomStack()

    # Проверяем начальное состояние стека
    assert stack.is_empty() == True
    assert str(stack) == "[]"

    # Проверяем push и pop
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert str(stack) == "[1, 2, 3]"

    assert stack.peek() == 3
    popped = stack.pop()
    assert popped == 3
    assert str(stack) == "[1, 2]"

    # Проверяем исключения
    try:
        stack.pop()
        stack.pop()
        stack.pop()
    except StackError as e:
        assert str(e) == "Pop from an empty stack"

    try:
        stack.peek()
    except StackError as e:
        assert str(e) == "Peek from an empty stack"

    # Проверяем итерацию
    stack.push(4)
    stack.push(5)
    elements = [item for item in stack]
    assert elements == [4, 5]

    # Проверяем пустой стек
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True
