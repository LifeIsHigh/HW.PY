    # Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input("Enter the dimension of the array: "))
X = int(input("Enter val X: "))
from random import randint
list = []
count = 0
for i in range(N):
    #list.append(i + 1)
    list.append(randint(0, 10))
    if X == list[i]:
        count += 1


# print(list)
# print(f"The value of {X} occurs {count} times")



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("Enter the dimension of the array: "))
X = int(input("Enter val X: "))
from random import randint
list_1 = []
temp_list = []
min = 0
max = 0
for i in range(N):
    list_1.append(randint(0, 10))

print(list_1)

MinTemp = -1
MaxTemp = 1000
MaxVal = list_1[i]

for i in range(len(list_1)):
    if MinTemp < list_1[i] and list_1[i] < X: 
        MinTemp = list_1[i]
        min = i
    elif MaxVal < list_1[i]:
        MaxVal = list_1[i]
for j in range(len(list_1)):
    if list_1[j] < MaxTemp and list_1[j] > X:
        MaxTemp = list_1[j]
        max = j

print(f"{MinTemp}: {min}")
print(f"{MaxTemp}: {max}")

if X - MinTemp <= MaxTemp - X:
    print(f"Result --> {list_1[min]}")
else:
    print(f"Result --> {list_1[max]}")
    

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с 
# английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12




word = input("Enter Word: ").upper()

dictionary = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

Result = 0
for i in word:
    for item in dictionary.items():
        if i in item[1]:
            Result += item[0]
print(f"Result --> {Result}")