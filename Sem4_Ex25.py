'''
Задача No25. Решение в группах
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
'''

stroka = 'a a a b c a a d c d d'

stroka_2 = stroka.split(' ')

slovar = dict()

for i in stroka_2:
    if i in slovar:
        slovar[i] += 1
        print(f'{i}_{slovar[i]}', end=' ')
    else:
        slovar[i] = 0
        print(i, end=' ')