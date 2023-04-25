import json
from datetime import datetime


def main_menu():
    print(' ')
    menu_list = [
                    'Создать заметку',
                    'Показать все заметки',
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

    with open('notes.json', encoding='UTF-8') as file:
        data = json.load(file)
        count = 0
        for ii in data['Notes']:
            count +=1
        id = {'id': count + 1} 
        new_data, id = id, new_data
        new_data.update(id)
        date = datetime.now().strftime('%d.%m.%y')
        new_data['date'] = date  
        data["Notes"].append(new_data)    

    return data


def print_all(my_list : list):
    print('\n',*my_list, sep='')




def edit_notes():
    number = int(input('Введите id заметки: '))

    with open('notes.json', encoding='UTF-8') as file:
        data = json.load(file)

        for ii in data['Notes']:
            if (ii['id'] == number):
                ii['heading'] = input('Введите заголовок заметки: ')
                ii['note body'] = input('Введите тело заметки: ')
                ii['date'] = datetime.now().strftime('%d.%m.%y')

    return data            

def delete_notes():
    number = int(input('Введите id заметки: '))
    with open('notes.json', encoding='UTF-8') as file:
        data = json.load(file)
        
        data['Notes'].pop(number-1)
        count = 1
        for ii in data['Notes']:
            ii['id'] = count
            count +=1

    return data        




