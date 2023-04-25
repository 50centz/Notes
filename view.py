import json
from datetime import datetime
import time

def main_menu():
    print(' ')
    menu_list = [
                    'Создать заметку',
                    'Показать все заметки',
                    'Показать заметку по дате',
                    'Изменить заметку',
                    'Удалить заметку',
                    'Выход из программы'   
                ]
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    print(' ')    
    user_choice = int(input('Введи пункт: '))
    return user_choice



def create_note():
    heading = input('Введите заголовок заметки: ')
    note_body = input('Введите тело заметки: ')

    new_data = {"heading" : heading, "note body" : note_body}  
    return new_data


def print_all(my_list : list):
    print('\n',*my_list, sep='')


def date():
    print('Шаблон для даты: 01.01.01')
    date = input('Введите дату заметки: ')
    start = True
    while start:
        try:
            valid_date = time.strptime(date, '%d.%m.%y')
            start = False
        except ValueError:
            print('\nНекорректная дата !\n')
            print('Шаблон для даты: 01.01.01')
            date = input('Введите дату заметки: ')
    return date

def show_by_date(my_list : list):
    if (len(my_list) == 0):
        print('\n' 'На эту дату нет записей !')
    else:
        print('\n',*my_list, sep='')


def edit_notes():
    number = input('Введите id заметки: ')
    start = True
    while start:
        try:
            int(number)
            start = False
            number = int(number)
        except ValueError:
            print('\nЭто не число !\n')
            number = input('Введите id заметки: ')

    with open('notes.json', encoding='UTF-8') as file:
        data = json.load(file)

        count = 0

        for ii in data['Notes']:
            count += 1
        
        if (count < number):
            print('\nТакого id нет в заметках !')
        else:    
            for ii in data['Notes']:
                if (ii['id'] == number):
                    ii['heading'] = input('Введите заголовок заметки: ')
                    ii['note body'] = input('Введите тело заметки: ')
                    ii['date'] = datetime.now().strftime('%d.%m.%y')
                    ii['time'] = datetime.now().strftime('%H:%M:%S')
   
    return data            

def delete_notes():
    number = input('Введите id заметки: ')
    start = True
    while start:
        try:
            int(number)
            start = False
            number = int(number)
        except ValueError:
            print('\nЭто не число !\n')
            number = input('Введите id заметки: ')

    with open('notes.json', encoding='UTF-8') as file:
        data = json.load(file)

        count = 0

        for ii in data['Notes']:
            count += 1
        
        if (count < number):
            print('\nТакого id нет в заметках !')
        else:    
            data['Notes'].pop(number-1)
            count = 1
            for ii in data['Notes']:
                ii['id'] = count
                count +=1

    return data        




