# связь между view и db

from view import * # импортируется всё, что в файле есть
from db import *

def main():
     while True:
          res = select_op()
          match res:
                case 1:
                    add_info(get_info())
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    search_info(search())
                case 5:
                    print(book_view())
                case 6:
                    break

main()