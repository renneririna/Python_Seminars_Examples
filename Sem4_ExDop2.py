'''
Напишите программу, которая отделяет положительные элементы массива от отрицательных: 
переставляет все положительные (в том же порядке) в начало массива, 
а все отрицательные (в том же порядке) – в конец массива, 
все нулевые элементы должны оказаться в середине массива.

Входные данные
Первая строка содержит размер массива N. 
Во второй строке через пробел задаются N чисел – элементы массива. 
Гарантируется, что 0 < N ≤ 10000 .

Выходные данные
Программа должна вывести в одну строчку все элементы получившегося массива, разделив их пробелами.

Примеры
входные данные
6
1 -1 2 -2 0 3
выходные данные
1 2 3 0 -1 -2
'''

# Очищает консоль
# import os
# clear = lambda: os.system('cls')
# clear()

numbers = list(map(int, input().split()))

numbers_negative = []

count = 0

for i in range(len(numbers) - 1, -1, -1):
# первая -1 - отнимаем от длины списка -1 чтоб получить последний индекс
# вторая -1 - до какого индекса итерируемся
# третья -1 - шаг
    if numbers[i] < 0:
        numbers_negative.append(numbers.pop(i))
    if numbers[i] == 0:
        numbers.pop(i)
        count +=1
    
numbers_negative.reverse()

numbers += [0*count] + numbers_negative

print(' '.join(list(map(str, numbers))))