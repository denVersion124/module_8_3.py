def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    try:
        for number in numbers:
            try:
                result += number  # Приводим к float для суммирования
            except (TypeError, ValueError) as e:
                print(f'Некорректный тип данных для подсчёта суммы - {number}')
                incorrect_data += 1
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

    return result, incorrect_data


def calculate_average(numbers):
    try:
        total, incorrect_count = personal_sum(numbers)
        count = len(numbers) - incorrect_count  # Мы вычитаем некорректные данные

        if count == 0:
            raise ZeroDivisionError

        return total / count
    except ZeroDivisionError:
        return 0
    except TypeError:

        return None


# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

