import logging
import string
from collections.abc import Iterable
from typing import Dict, List, Optional

"""
№ 1 Реализовать класс MultiTempAttributes, который позволяет временно изменять значения атрибутов объекта.
Этот класс должен поддерживать контекстный менеджер, который изменяет указанные атрибуты объекта на новые значения,
а после завершения работы с объектом автоматически восстанавливает исходные значения атрибутов.

Класс MultiTempAttributes должен реализовывать следующие методы:

__init__(self, obj, attrs_values): Конструктор, принимающий два аргумента:

obj: Объект, атрибуты которого будут временно изменяться.
attrs_values: Словарь, где ключи — это имена атрибутов, которые нужно изменить, а значения — новые значения для этих атрибутов.
__enter__(self): Метод, который сохраняет исходные значения указанных атрибутов и устанавливает новые значения.

__exit__(self, exc_type, exc_value, traceback): Метод, который восстанавливает исходные значения атрибутов после выхода из контекстного менеджера, независимо от того, произошла ли ошибка.
"""


# Контекстный менеджер
class MultiTempAttributes:
    def __init__(self, obj, attrs_values: Dict):
        self.obj = obj
        self.attrs_values = attrs_values
        self.original_values = {}  # хранение исходных значений

    def __enter__(self):
        for attr, value in self.attrs_values.items():
            if hasattr(self.obj, attr):
                self.original_values[attr] = getattr(self.obj, attr)
                setattr(self.obj, attr, value)
        return self.obj  # объект с измененными атрибутами

    def __exit__(self, exc_type, exc_value, traceback):
        for attr, value in self.original_values.items():
            setattr(self.obj, attr, value)


"""
№ 2 Подсчет уникальных слов

Вам дан текст в виде строки, содержащий слова и пунктуацию.
Напишите функцию, которая определяет количество уникальных слов в этом тексте. Для подсчета уникальных слов следует учитывать следующие условия:

Текст должен быть приведен к нижнему регистру, чтобы слова с разными регистрами считались одинаковыми.
Все знаки пунктуации должны быть удалены из текста.
После удаления пунктуации текст следует разбить на слова, разделенные пробелами.
Слово считается уникальным, если оно встречается в тексте только один раз после удаления пунктуации и приведения текста к нижнему регистру.
"""


def count_unique_words(text: str) -> int:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    unique_words = set()

    unique_words_count = 0

    for word in words:
        if word not in unique_words:
            unique_words_count += 1
            unique_words.add(word)

    return unique_words_count


"""
№ 3 Анализ четных чисел

Аргументы:
numbers: Список целых чисел.


Возвращаемое значение:
Словарь с ключами:
"count": Количество четных чисел.
"sum": Сумма четных чисел (или None, если четных чисел нет).
"average": Среднее значение четных чисел (или None, если четных чисел нет).
"max": Максимальное значение четных чисел (или None, если четных чисел нет).
"min": Минимальное значение четных чисел (или None, если четных чисел нет).
"""


def analyze_even_numbers(numbers: List[int]) -> Dict[str, Optional[float]]:
    even_numbers = [num for num in numbers if num % 2 == 0]

    if not even_numbers:
        return {
            "count": 0,
            "sum": None,
            "average": None,
            "max": None,
            "min": None,
        }

    result = {
        "count": len(even_numbers),
        "sum": sum(even_numbers),
        "average": sum(even_numbers) / len(even_numbers),
        "max": max(even_numbers),
        "min": min(even_numbers),
    }
    return result

"""
№ 4 Проверка уникальности элементов в вложенных структурах данных

Реализовать функцию all_unique_elements, которая проверяет,
содержатся ли в заданной структуре данных только уникальные элементы.

Поддерживаются следующие типы данных:
Строки
Списки
Кортежи
Множества
Вложенные структуры (например, списки внутри списков и т.д.)
Функция должна игнорировать значения типа None.
"""


def all_unique_elements(data) -> bool:
    def flatten(d):
        """Вспомогательная функция для рекурсивного разворачивания вложенных структур"""
        for el in d:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                yield from flatten(el)
            else:
                yield el

    seen = set()
    for item in flatten(data):
        if item is not None:
            if item in seen:
                return False
            seen.add(item)
    return True


"""
№ 5 

Напишите функцию enumerate_list,
которая принимает на вход список data и возвращает новый список,
содержащий элементы из data, но каждый элемент дополнен его индексом.
Индекс каждого элемента рассчитывается начиная с start и увеличивается на step для каждого следующего элемента.

Функция должна поддерживать следующие параметры:

data (list): список, элементы которого нужно перечислить.
start (int, по умолчанию 0): начальный индекс.
step (int, по умолчанию 1): шаг, на который увеличивается индекс.
recursive (bool, по умолчанию False): если True, функция должна рекурсивно обрабатывать вложенные списки.
Функция должна возвращать список, в котором каждый элемент является кортежем из двух элементов: индекса и значения из исходного списка.
"""


def enumerate_list(
    data: list, start: int = 0, step: int = 1, recursive: bool = False
) -> list:
    def recursive_enumerate(lst, idx):
        result = []
        for i, item in enumerate(lst):
            if recursive and isinstance(item, list):
                result.extend(recursive_enumerate(item, idx))
                idx += len(item)
            else:
                result.append((idx, item))
                idx += step
        return result

    if recursive:
        return recursive_enumerate(data, start)
    else:
        return [(start + i * step, item) for i, item in enumerate(data)]


"""
№ 6 Реализация контекстного менеджера для подключения к базе данных (симуляция)

Вам необходимо реализовать класс DatabaseConnection,
который будет управлять подключением к базе данных и транзакциями(симуляция в виде сообщений),
используя менеджер контекста. Класс должен поддерживать следующие функции:

Инициализация: При создании экземпляра класса, он должен принимать имя базы данных (db_name), к которой будет подключаться.

Менеджер контекста: Класс должен реализовывать методы __enter__ и __exit__, чтобы использовать его в блоке with. 
При входе в блок контекста должно происходить подключение к базе данных, а при выходе из блока — закрытие соединения и обработка возможных ошибок.

Подключение к базе данных: Метод connect должен инициировать подключение к базе данных и сохранять его состояние.

Выполнение запроса: Метод execute_query должен выполнять запрос, если активна транзакция. В противном случае должен выбрасываться исключение.

Управление транзакциями: Методы start_transaction, commit и rollback должны управлять транзакциями. Транзакция должна быть активна для выполнения запросов, и должна быть закрыта после коммита или отката.

Логирование: Класс должен использовать встроенный модуль logging для записи логов подключения, выполнения запросов, начала и завершения транзакций, а также для обработки ошибок.
"""

# Настройка логирования для примера
logging.basicConfig(level=logging.INFO)


class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
        self.transaction_active = False
        self.logger = logging.getLogger(__name__)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
        else:
            if self.transaction_active:
                self.commit()
        self.close()

    def connect(self):
        if self.connection is None:
            self.connection = f"Connected to {self.db_name} database"
            self.logger.info(f"Connected to database: {self.db_name}")

    def close(self):
        if self.connection is not None:
            self.connection = None
            self.logger.info(f"Disconnected from database: {self.db_name}")

    def execute_query(self, query: str):
        if self.transaction_active:
            return f"Result of '{query}'"
        else:
            raise RuntimeError("No active transaction")

    def start_transaction(self):
        if not self.transaction_active:
            self.transaction_active = True
            self.logger.info("Transaction started.")

    def commit(self):
        if self.transaction_active:
            self.transaction_active = False
            self.logger.info("Transaction committed.")
        else:
            raise RuntimeError("No active transaction to commit")

    def rollback(self):
        if self.transaction_active:
            self.transaction_active = False
            self.logger.info("Transaction rolled back.")
