#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


from random import randint


a = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(a):
    list.append(randint(-9, 9))

for i in range(len(list)):
    while i < len(list)/2 and a > len(list)/2:
        a = a - 1
        b = list[i] * list[a]
        list2.append(b)
        i += 1

print(list)
print(list2)

