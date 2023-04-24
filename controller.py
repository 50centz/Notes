import model
import view

def input_choice(ch):
    match ch:
        case 2:
            my_list = model.show_all_notes()
            view.print_all(my_list)
        case 6:
            model.exit_program()


def start():
    while True:
        choice = view.main_menu()
        input_choice(choice)