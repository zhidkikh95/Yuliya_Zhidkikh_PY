import os
import time
import datetime
import random
name = ""
def auth_check(func):
    def wrapper():
        if bool(name) is True:
            func()
        else:
            print("Вы не авторизованы\nДля авторизации нажмите 4")
    return wrapper
def func_1():
    today = datetime.datetime.now()
    new_year = datetime.datetime(2022,1,1)
    delta = new_year - today
    print (f"До Нового года осталось {delta.days} дней")
def func_2():
    print (f"Я загадал число {random.randint(1, 10)}")
@auth_check
def func_3():
    name_len = len(name)
    print (f"В Вашем имени {name_len} букв")
menu = """
        1 - Количество дней до Нового года
        2 - Случайное число от 1 до 10
        3 - Длина Вашего имени *требует авторизации
        4 - Вызов окна авторизации
        5 - Выход
        """
def menu_print():
    print(menu)
print(f"Вас приветствует помощник! \nЗдесь Вы можете получить доступ к следующей информации:\n{menu}")
time.sleep(5.0)
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    menu_print()
    if bool(name) is True:
        menu_num = int(input(f"{name}, выберите пункт меню: "))
    else:
        menu_num = int(input("Выберите пункт меню: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if menu_num == 1:
        func_1()
    elif menu_num == 2:
        func_2()
    elif menu_num == 3:
        func_3()
    elif menu_num == 4:  
        name = input('Введите Ваше имя: ')
    elif menu_num == 5: 
        break
    else:
        print("Ошибка ввода")
   