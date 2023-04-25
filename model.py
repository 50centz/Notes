import json
from pprint import pprint
from datetime import datetime


   
def write_notes(data):
    with open('notes.json', 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)



def create_note(new_data):
    with open('notes.json', encoding='UTF-8') as file:
        data = json.load(file)
        count = 0
        for ii in data['Notes']:
            count +=1
        id = {'id': count + 1} 
        new_data, id = id, new_data
        new_data.update(id)
        date = datetime.now().strftime('%d.%m.%y')
        time = datetime.now().strftime('%H:%M:%S')
        new_data['date'] = date
        new_data['time'] = time  
        data["Notes"].append(new_data)

    write_notes(data)     



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
        my_list.append('  Время заметки: ' + str(ii['time']) + '\n')
    return my_list  



    
def date(date):
    with open('notes.json', encoding='UTF-8') as file:
        data = json.load(file)

    my_list = []
    for ii in data['Notes']:
        if (str(ii['date']) == date):
            my_list.append('id заметки: ' + str(ii['id']) + '\n')
            my_list.append('  Заголовок: ' + str(ii['heading']) + '\n')
            my_list.append('  Тело заметик: ' + str(ii['note body']) + ' ' + '\n')
            my_list.append('  Дата заметки: ' + str(ii['date']) + '\n')
            my_list.append('  Время заметки: ' + str(ii['time']) + '\n')
    return my_list        




def exit_program():
    print('Завершение программы')
    exit()