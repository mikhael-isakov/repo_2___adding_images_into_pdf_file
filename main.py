from classes import *
from functions import * 


entry_list = []
entry_text_list = []


def main(): 
    '''Функция создаёт экземпляр главного окна, и запускает главный цикл'''
    app = MainWindow(entry_list, entry_text_list)
    app.draw_main_menu(entry_list, entry_text_list)
    app.draw_widjets(entry_list, entry_text_list)
    app.window.mainloop()


if __name__ == '__main__':
    main()
