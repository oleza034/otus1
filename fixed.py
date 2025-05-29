"""
Вычисление среднего значения для набора
"""

# Функция вычисления среднего значения
def calculate_average(list_of_numbers: list[int | float]) -> int | float | None:
    """
    Вычисляет среднее значение
    :param list_of_numbers: Список значений для вычисления среднего
    :return: Среднее значение
    """
    # Проверка валидности входящего значения
    if not(isinstance(list_of_numbers, list) and
           all(type(n) in (int, float) for n in list_of_numbers)):
        return None
    # Вычисление среднего
    total_value= sum(list_of_numbers)
    length = len(list_of_numbers)
    average = total_value / length

    # Вывод результата
    return average


# Входные данные
numbers = [10, 15, 20]
# Вызов функции вычисления среднего значения
result = calculate_average(numbers)
# Печать результата
print("The average is:", result)
