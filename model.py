import json
from pprint import pprint


   
def write_notes(data):
    with open('notes.json', 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)





def show_all_notes():
    with open('notes.json', 'r', encoding='UTF8') as file:
        text = json.load(file)
        #pprint(text)
        
    my_list = []
    for ii in text['Notes']:
        my_list.append('id заметки: ' + str(ii['id']) + '\n')
        my_list.append('  Заголовок: ' + str(ii['heading']) + '\n')
        my_list.append('  Тело заметик: ' + str(ii['note body']) + ' ' + '\n')
        my_list.append('  Дата заметки: ' + str(ii['date']) + '\n')
    return my_list  

    



def exit_program():
    print('Завершение программы')
    exit()