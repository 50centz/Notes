import model
import view

def input_choice(ch):
    match ch:
        case 1:
            data = view.create_note()
            model.write_notes(data)
        case 2:
            my_list = model.show_all_notes()
            view.print_all(my_list)
        case 3:
            data = view.edit_notes()
            model.write_notes(data)
        case 4:
            data = view.delete_notes()
            model.write_notes(data)        
        case 5:
            model.exit_program()


def start():
    while True:
        choice = view.main_menu()
        input_choice(choice)