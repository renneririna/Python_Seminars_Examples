# функции для работы с базаой данных

def add_info(arg):
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(arg)

def search_info(arg):
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
        res = []
        count = 1
        for i in range(len(lst)):
            if arg in lst[i]:
                res.append(lst[i])
                print(f'{count}. {lst[i]}')
                count += 1
        return res
    
def book_view():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        return file.read()