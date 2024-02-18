'''
Задача No35. Решение в группах
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n (само число)

Input: 5 
Output: yes
'''

def prime_number(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input('Input number: '))

if prime_number(number):
    print('YES')
else:
    print('NO')