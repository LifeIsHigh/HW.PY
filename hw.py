# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


'''
a1 = int(input("Enter first element: "))
d = int(input("Ender d: "))
n = int(input("Enter size array: "))

for i in range(n):
    print(a1 + (i) * d, end=' ')
'''


# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


array_1 = list(map(int, input("Enter the array separated by a space: ").split()))
max = int(input("Enter max value: "))
min = int(input("Enter min value: "))
array_2 = []
for i in range(len(array_1)):
    if array_1[i] >= min and array_1[i] <= max:
        array_2.append(i)
print(array_2)
