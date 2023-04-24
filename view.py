



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
    return user_choice


def print_all(my_list : list):
    print(*my_list)
