'''
Задача No17. Решение в группах
Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4] 
Output: 6

Примечание: 
Пользователь может вводить значения списка или список задан изначально.
'''

a = [1, 1, 2, 0, -1, 3, 4, 4]

b = set(a)

print(len(b))

b = []

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)