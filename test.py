import json
from pprint import pprint


def show_all_notes():
    with open('notes.json', 'r', encoding='UTF8') as file:
        text = json.load(file)
        pprint(text)
        

    for txt in text['personal']:
        print(txt['name'] , ':', txt['salary']) 

show_all_notes()        