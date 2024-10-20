"""Задача:
Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
Необходимо создать 2 генераторных сборки:
В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк
из списков first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк
в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip.
Используйте функции range и len.

Пример результата выполнения программы:
Пример выполнения кода:
print(list(first_result))
print(list(second_result))
Вывод в консоль:
[1, 2]
[False, False, True]
Примечания:
Это небольшая практика, поэтому важность выполнения каждого условия обязательна."""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Для first_result мы используем zip, чтобы объединять строки из обоих списков и вычислять разницу их длин
# только для тех, где длины не равны.
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Для second_result используем range и len, чтобы сравнить длины строк в одинаковых позициях.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример выполнения
print(list(first_result))  # Вывод разницы длин строк
print(list(second_result))  # Вывод результатов сравнения длин
