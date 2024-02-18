'''
Сделайте функцию, которая будет возвращать элементы объекта, параметром получая
строку с ключами объекта, разделенными точками:
func('a, b, c'); вернет '+++'
'''
def find_plus(dct: dict, stroka: str):
    find_key = stroka.split(".")[0]
    if len(stroka) == 1:
        return dct[find_key]
    for key in dct:
        if key == find_key:
            return find_plus(dct[key], stroka[2:])

nested_dict = {
    'a': {
        'b': {
            'c': '+++'
        }
    }
}
print(find_plus(nested_dict, 'a.b.c'))