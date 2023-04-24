import json
from pprint import pprint

def choice(inp):
    match inp:
        # case 1:
        #    create_Notes()
        case 2:
          show_all_notes()  
        # case 3:

        # case 4:

        # case 5:
        case 6:
            exit_program()
   


def show_all_notes():
    with open('notes.json', 'r', encoding='UTF8') as file:
        text = json.load(file)
        pprint(text)

    for txt in text:
        print(txt['name'] , ':', txt['salary'])    

    



def exit_program():
        print('Завершение программы')
        exit()