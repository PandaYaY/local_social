import msvcrt
import os
import json
from datetime import datetime
import blohi

menu = {
    'Личная информация': {
        'Имя': {},
        'Фамилия': {},
        'Дата рождения': {},
        'Возраст': {},
    },
    'Игрушки': {
        'Блохи': {},
    },
    'Сменить пароль': {},
    'Удалить аккаунт': {},
    'Выйти с аккаунта': {},
}


def date_format(date_exp):  # обработка даты в list
    date_exp = date_exp.replace(date_exp[2], '.').split('.')
    date_exp = list(map(lambda x: int(x), date_exp))
    return date_exp


def skoka_let(day):  # подсчёт сколько лет
    day = date_format(day)

    dategg = datetime.date(datetime.today())
    dategg = str(dategg).split('-')
    dategg = list(map(lambda x: int(x), dategg))
    dategg[0], dategg[2] = dategg[2], dategg[0]

    years = dategg[2] - day[2]
    months = dategg[1] - day[1]
    days = dategg[0] - day[0]

    if days < 0:
        months -= 1
    if months < 0:
        years -= 1

    return years


def search_user(login, data):  # сёрч юзер
    for acc in data:
        if data[acc]['join']['login'] == login:
            return data[acc]
    return False


def help(menu, deep=0):
    for i, item in enumerate(menu):
        chr = ' ' * deep + str(i+1) + '. '
        print(chr + item)
        if menu[item]:
            help(menu[item], deep+4)
    return False


def register():  # регистрация
    os.system('cls')  # очистка экрана
    vse_huynya = 'Пароль не совпадает!'  # прикол

    with open('Data.json', 'r') as file:
        data = json.load(file)

    while True:
        login = input('Логин: ')
        if not search_user(login, data):
            break

        os.system('cls')  # очистка экрана
        print('Такой пользователь уже существует')

    while True:  # проверка пароля

        password = input('Пароль: ')
        password2 = input('Подтвердите пароль: ')

        if password == password2:
            name = input('Введите имя: ')
            s_name = input('Введите фамилию: ')

            birthday = input('дата рождения(дд.мм.гггг): ')
            birthday = birthday.replace(birthday[2], '.')
            break

        print(vse_huynya)
        vse_huynya += '!!!'  # увилечение прикола

    accaunt = {
        'join': {
            'login': login,
            'password': password,
        },
        'info': {
            'name': name,
            's_name': s_name,
            'birthday': birthday,
        },
        'games': {
            'blohi': 0,
        },
    }

    with open('Data.json', 'r', encoding='utf-8') as read:  # !!!запись. ДА!

        data = json.load(read)
        data[login + password] = accaunt

        with open('Data.json', 'w', encoding='utf-8') as write:
            json.dump(data, write)

    return False


def login_in():  # вход в аккаунт
    os.system('cls')  # очистка экрана

    login = input('Логин: ')
    password = input('Пароль: ')

    with open('Data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    accaunts = data.get(login + password, False)

    trys = 0
    while not accaunts:
        os.system('cls')

        trys += 1
        if trys > 1:
            found = search_user(login, data)
            if found:
                years = int(input('Забыл пароль???\nСколько тебе лет?: '))
                acc_years = skoka_let(found['info']['birthday'])
                if years == acc_years:
                    new_password(found)
                else:
                    print('Такого аккаунта нет!')
                return False

        print('Миша, всё хуйня, давай по новой!')
        login = input('Логин: ')
        password = input('Пароль: ')

        accaunts = data.get(login + password, False)

    return accaunts


def info(data):
    os.system('cls')

    years = skoka_let(data["info"]["birthday"])

    print(f'Имя: {data["info"]["name"]},\n'
          f'Фамилия: {data["info"]["s_name"]},\n'
          f'Дата рождения: {data["info"]["birthday"]},\n'
          f'{years} лет')

    print(f'Press any key to return...')
    msvcrt.getch().decode()

    return login_true(data)


def games(data):
    os.system('cls')

    print('___Игры___')

    games_list = {
        '1': lambda: blohi.game(),
        'p': lambda: print('Hallo'),

        'help': lambda: help(menu),
    }

    number = input('Цифорка: ')

    result = games_list.get(number, False)()

    # def zatirka():
    #     return

    if number == '1':
        print('красава')
    return False


def change_password(data):
    os.system('cls')

    password = input('Введите пароль: ')
    while password != data["join"]["password"]:
        os.system('cls')
        password = input('Неверный пароль!\nВведите пароль: ')
    new_password(data)


def new_password(data):
    new_password = input('Введите новый пароль: ')
    check = input('Подтвердите пароль: ')
    while new_password != check:
        new_password = input('Пароли не совпали!\nВведите новый пароль: ')
        check = input('Подтвердите пароль: ')

    with open('Data.json', 'r', encoding='utf-8') as file:
        change = json.load(file)

    key = data['join']['login'] + data['join']['password']
    change[key]['join']['password'] = new_password
    inf = change[key]
    change.pop(key)
    new_key = inf['join']['login'] + inf['join']['password']
    change[new_key] = inf

    with open('Data.json', 'w', encoding='utf-8') as file:
        json.dump(change, file)

    return change[new_key]


def delete_accaunt(data):
    os.system('cls')

    key = input('Вы уверены, что хотите удалить аккаунт?\n'
                'Введите (yes): ')

    if key == 'yes' or key == 'Yes':
        with open('Data.json', 'r', encoding='utf-8') as file:
            all_data = json.load(file)

        name = data['join']['login'] + data['join']['password']
        all_data.pop(name)

        with open('Data.json', 'w', encoding='utf-8') as file:
            json.dump(all_data, file)
        return 'exit'
    return False


def start_menu():
    os.system('cls')  # очистка экрана

    print('Выберите пункт меню:\n'
          '1. Войти в аккаунт\n'
          '2. Регистрация\n'
          '3. FAQ')

    number = input('Цифорка: ')

    while number == '3':
        os.system('cls')  # очистка экрана

        print('Выберите пункт меню:\n'
              '1. Войти в аккаунт\n'
              '2. Регистрация\n'
              '3. FAQ\n'
              '\nПрикол, да?!\nВведи ссаные цифры(1 или 2).\n')

        number = input('Цифорка: ')

    spisok = {
        '1': lambda: login_in(),
        '2': lambda: register(),
    }
    data = spisok.get(number, lambda: False)()

    return data


def login_true(data):
    os.system('cls')  # очистка экрана
    # print(data)

    print(f'Здарова, {data["info"]["name"]}!')
    number = input('Цифорка: ')

    spisok = {
        '1': lambda: info(data),
        '2': lambda: games(data),
        '3': lambda: change_password(data),
        '4': lambda: delete_accaunt(data),
        '5': lambda: 'exit',
        'help': lambda: help(menu),
        'Help': lambda: help(menu),
    }

    return spisok.get(number, lambda: False)()


def authoryse():
    state = start_menu()  # возвращает данные
    if state:  # проверка на цифорки и выход в логин тру
        return state
    return False


if __name__ == '__main__':
    while True:
        state = authoryse()

        while state:
            login_state = login_true(state)  # залогинен
            if login_state == 'exit':
                break
# a = {}
# games(a)
