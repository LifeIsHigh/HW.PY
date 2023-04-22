# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания 
# # все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# # m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = [int(i) for i in input('Enter the first list of values separated by a space: ').split()]
n_set = list(n)

print(n)
SortedN = filter(lambda x: n_set.count(x) == 1, n_set)
SortedN = set(SortedN)
print(SortedN)

m = [int(i) for i in input('Enter the second list of values separated by a space: ').split()]
m_set = list(m)

print(m)
SortedM = filter(lambda x: m_set.count(x) == 1, m_set)
SortedM = set(SortedM)
print(SortedM)
      
Result=sorted(SortedN & SortedM)
print(Result)



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
from random import randint
n = int(input('Enter the number of shrubes in the garden:'))
Result = 0

if n < 3:
    print("An incorrect value for the number of shrubes was entered.")
else:
    N = list(randint(1, 10) for i in range(n))
    X = int(input('Enter the shrub number: '))
    if X == len(N):
        Result = N[-2] + N[X - 1] + N[0]
    elif X == 1:
        Result = N[X] + N[X - 1] + N[-1]
    else:
        Result = N[X - 2] + N[X-1] + N[X]
    
    print(N)
    print(Result)