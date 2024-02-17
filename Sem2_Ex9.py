'''
Задача No9. Решение в группах
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while
Input: 5
Output: 120
'''
n = int (input())
res =  1
m = 1
while  n >= m:
    res  *= m
    m  += 1 
print (res)

# Другое решение

num = int(input("Input a number: "))
i = 1
fac = 1
while (i <= num):
    fac = fac * i
    i += 1
print(fac)