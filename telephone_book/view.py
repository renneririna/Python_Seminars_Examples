# функции для работы с пользователем, связь между сервером и пользователем

def select_op():
    op = int(input('Выбери что хочешь сделать:\n'
                   '1-Создать контакт\n'
                   '2-Удалить контакт\n'
                   '3-Изменить контакт\n'
                   '4-Показать контакт\n'
                   '5-Посмотреть все контакты\n'
                   '6-Выход'))
    return op

def get_info():
    name = input("Введи ФИО: ")
    number = input("Введи номер тедефона: ")
    data = name + " --> " + number
    return data

def search():
    return input('Поиск:\n')