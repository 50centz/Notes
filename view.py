



def main_menu():
    print(' ')
    menu_list = [
                    'Создать заметку',
                    'Показать все заметки',
                    'Изменить заметку',
                    'Сохранить заметку',
                    'Удалить заметку',
                    'Выход из программы'   
                ]
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    print(' ')    
    user_choice = int(input('Введи пункт: '))
    if (user_choice == 1):
        createNotes()
    if (user_choice == 2):
        return user_choice
    if (user_choice == 3):
        editNotes()
    if (user_choice == 4):
        saveNotes()
    return user_choice            
