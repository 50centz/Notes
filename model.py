import json
from pprint import pprint


   


def show_all_notes():
    with open('notes.json', 'r', encoding='UTF8') as file:
        text = json.load(file)
        #pprint(text)
        
    my_list = []
    for txt in text['Notes']:
        my_list.append('id заметки: ' + str(txt['id']) + '\n')
        my_list.append('  Заголовок: ' + str(txt['heading']) + '\n')
        my_list.append('  Тело заметик:' + str(txt['note body']) + ' ' + '\n')
    return my_list  

    



def exit_program():
    print('Завершение программы')
    exit()