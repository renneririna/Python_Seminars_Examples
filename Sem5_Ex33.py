'''
Задача No33. Решение в группах
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4 
Output: 1 3 3 3 1
'''

n = int(input())
max_number = 0
min_number = 6
a = []

for i in range(n):
    temp = int(input())
    a.append(temp)
    if max_number < temp:
        max_number = temp
    if min_number > temp:
        min_number = temp

for i in range(len(a)):
    if a[i] == max_number:
        a[i] = min_number
print(*a)


# Другое решение

grades = [int(input('Input grades: ')) for i in range(int(input('Input number of grades: ')))]

for i in range(grades.count(max(grades))):
    grades[grades.index(max(grades))] = grades[grades.index(min(grades))]
print(*grades)