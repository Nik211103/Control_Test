﻿# Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк, 
# длина которых меньше, либо равна 3 символам. 
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.


# def filter_strings(strings):
#     new_array = []
#     for string in strings:
#         if len(string) <= 3:
#             new_array.append(string)
#     return new_array

def filter_strings(strings):
    return list(filter(lambda s: len(s) <= 3, strings))

input_array = input("Введите элементы массива через пробел: ").split()
result_array = filter_strings(input_array)
print("Новый массив:", result_array)