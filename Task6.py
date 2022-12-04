"""6) Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении  числа 10 завершаем цикл. Во втором также необходимо
предусмотреть условие, при котором повторение элементов списка будет
прекращено."""

from itertools import count, cycle

# start_digit = int(input("Введите стартовое число: "))
# final_digit = int(input("Введите конечное число: "))
# for el in count(start_digit):
#     if el > final_digit:
#         break
#     print(el)

orig_list = ['Hello', 123, True]
for i, el in enumerate(cycle(orig_list)):
    if i > 3:
        break
    print(el)