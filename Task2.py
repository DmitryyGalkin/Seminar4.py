"""2) Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""
import random

original_list = [random.randint(1, 30) for x in range(1, 10)]
print(original_list)
result_list = [el for num, el in enumerate(original_list) if
               original_list[num] > original_list[num - 1]]
print(result_list)
