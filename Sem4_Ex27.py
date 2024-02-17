'''
Задача No27. Решение в группах
Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

Output: 13
'''
text = 'She sells sea shells on the sea shore The shells '\
'that she sells are sea shells I"m sure.So if she sells sea '\
'shells on the sea shore I"m sure that the shells are sea shore shells'

text = text.replace('.', ' ').lower()
text_red = text.split(' ')
text_res = set(text_red)
print(text_res)
print(len(text_res))


# Сокращенное решение
#print(len(set(text.replace('.', ' ').lower().split(' '))))