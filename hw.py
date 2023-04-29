# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

A = int(input("Enter a value A: "))
B = int (input("Enter a value B: "))

def PositivExponentiation (A, B):
    if B == 0:
        return 1
    x = PositivExponentiation(A, B-1)
    return A*x
 
def NegativExponentiation(A, B):
    if B == 0:
        return 1
    x = NegativExponentiation(A, B+1)
     
    return 1/A*x
    
if B >= 0:
    print(PositivExponentiation (A, B))
else:
    print(NegativExponentiation (A, B))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

def Summ(a, b):
    if b == 0:
        return a
    x = Summ(a + 1, b - 1)
    return x
print(Summ(a, b))
