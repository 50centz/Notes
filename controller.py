import model
import view




def start():
    while True:
        choice = view.main_menu()
        model.choice(choice)