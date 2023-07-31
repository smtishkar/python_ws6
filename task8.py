# Создайте пакет с всеми модулями, которые вы создали за время занятия. 
# Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
# В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.


import pack_of_tasks.task7
# from pack_of_tasks import task7
# from pack_of_tasks.task7 import date_check
# from pack_of_tasks import


date = '29.02.2004'
print(pack_of_tasks.task7.date_check(date))
# print(pack_of_tasks.task7.date_check(date))
# print(pack_of_tasks.task7.date_check(date))




