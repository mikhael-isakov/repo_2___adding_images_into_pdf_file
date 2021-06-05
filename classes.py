from tkinter import Tk, Toplevel, Menu, Frame, LabelFrame, Label, Button
from functions import *


class OverButton(Button):
    '''Класс определяет кнопки, изменяющие свой цвет и цвет текста при событиях'''
    def __init__(self, window, **kwargs):
        Button.__init__(self, window, **kwargs)
        self.bind('<Enter>', self.if_enter)
        self.bind('<Leave>', self.if_leave)        
        self.bind('<Button-1>', self.if_click)

    def if_enter(self, event):
        self['bg'] = '#003E00'
        self['fg'] = '#FFFFFF'
        self['activebackground'] = '#003E00'

    def if_leave(self, event):
        self['bg'] = '#CBF5AF'
        self['fg'] = '#000000'

    def if_click(self, event):
        self['bg'] = '#CBF5AF'
        self['fg'] = '#000000'


class MainWindow:
    '''Класс определяет главное окно приложения'''
    def __init__(self, entry_list, entry_text_list):
        self.window = Tk()
        self.window.title ('Программа вставки изображений в файлы .pdf')
        self.window.geometry('465x450+300+250')
        self.window.resizable(False, False)
        
    def draw_main_menu(self, entry_list, entry_text_list):
        '''Метод реализует отображение главного меню'''
        main_menu = Menu(self.window) 
        self.window.config(menu = main_menu) 
        # формирование подпунктов пункта меню 'Файл'
        menu_file = Menu(main_menu, tearoff=0)
        menu_file.add_command(label = 'Вставить изображение и сохранить в новый файл.pdf', 
                              command = lambda: image_to_pdf(ChildWindow, self.window, 
                                                             entry_list, entry_text_list))
        menu_file.add_separator()
        menu_file.add_command(label = 'Выход', command = lambda: my_exit())
        # формирование подпунктов пункта меню 'Справка' 
        menu_help = Menu(main_menu, tearoff=0)
        text1 = 'Программа предназначена\nдля вставки изображений\nв файлы .pdf'
        menu_help.add_command(label = 'О программе', 
                              command = lambda: ChildWindow(self.window, title='О программе', 
                                                            text=text1, autoclosed_time=5000))
        # добавление приготовленных пунктов меню в меню   
        main_menu.add_cascade(label = 'Файл', menu=menu_file)
        main_menu.add_cascade(label = 'Справка', menu=menu_help) 
       
    def draw_widjets(self, entry_list, entry_text_list): 
        '''Метод реализует отображение всех элементов GUI, кроме главного меню'''
        
        self.window.grid_columnconfigure(0, minsize=200)
        self.window.grid_columnconfigure(1, minsize=200)
        
        frame_0 = Frame(self.window, padx=10) 
        frame_0.grid(row=0, column=0, columnspan=2, stick='we', pady=10, padx=5)
        Label(frame_0, text='Программа вставки изображений в файлы .pdf', 
              font='Arial 12 bold').pack(side='top') 

        frame_1 = LabelFrame(self.window, text=' Имя файла .pdf в текущем каталоге ') 
        frame_1.grid(row=1, column=0, stick='we', pady=5, padx=5)
        create_entry(frame_1, 27, entry_list, entry_text_list)
        entry_list[0].pack(side='left')

        frame_2 = LabelFrame(self.window, text=' Номер страницы ') 
        frame_2.grid(row=2, column=0, stick='we', pady=5, padx=5)
        Label(frame_2, text =' n = ', font = 'Arial 12').pack(side='left') 
        create_entry(frame_2, 5, entry_list, entry_text_list)
        entry_list[1].pack(side='left') 

        frame_3 = LabelFrame(self.window, text=' Имя файла с изображением в тек. кат.') 
        frame_3.grid(row=3, column=0, stick='we', pady=5, padx=5)
        create_entry(frame_3, 27, entry_list, entry_text_list)
        entry_list[2].pack(side='left')
        
        frame_4 = LabelFrame(self.window, text=' Координаты левого верхнего угла ') 
        frame_4.grid(row=4, column=0, stick='we', pady=5, padx=5)
        Label(frame_4, text ='прямоугольной области, \nв центр которой\nбудет вставлено изображение', 
              font = 'Arial 10').pack(side='top')
        Label(frame_4, text ='   x = ', font = 'Arial 12').pack(side='left') 
        create_entry(frame_4, 5, entry_list, entry_text_list)
        entry_list[3].pack(side='left') 
        Label(frame_4, text ='     ', font = 'Arial 12').pack(side='left') 
        Label(frame_4, text ='   y = ', font = 'Arial 12').pack(side='left') 
        create_entry(frame_4, 5, entry_list, entry_text_list)
        entry_list[4].pack(side='left') 
                
        frame_5 = LabelFrame(self.window, text=' Размер прямоугольной области ') 
        frame_5.grid(row=5, column=0, stick='we', pady=5, padx=5)
        Label(frame_5, text ='в центр которой\nбудет вставлено изображение', 
              font = 'Arial 10').pack(side='top')
        Label(frame_5, text ='ширина ', font = 'Arial 12').pack(side='left') 
        create_entry(frame_5, 5, entry_list, entry_text_list)
        entry_list[5].pack(side='left')  
        Label(frame_5, text ='   ', font = 'Arial 12').pack(side='left') 
        Label(frame_5, text ='высота ', font = 'Arial 12').pack(side='left') 
        create_entry(frame_5, 5, entry_list, entry_text_list)
        entry_list[6].pack(side='left') 
        
        frame_6 = LabelFrame(self.window, text=' Имя выходного файла .pdf ') 
        frame_6.grid(row=6, column=0, stick='we', pady=5, padx=5)
        create_entry(frame_6, 27, entry_list, entry_text_list)
        entry_list[7].pack(side='left') 
        
        Button_1 = OverButton(self.window, text = 'ВСТАВИТЬ\nИЗОБРАЖЕНИЕ\nИ СОХРАНИТЬ\n В НОВЫЙ\nФАЙЛ .pdf', 
                              bg='#CBF5AF', fg='#000000', 
                              command = lambda: image_to_pdf(ChildWindow, self.window, 
                                                             entry_list, entry_text_list))
        Button_1.grid(row=1, column=1, rowspan=6, stick='wens', padx=5, pady=5)

        
class ChildWindow:
    '''Класс определяет дочерние окна, выводящие различные сообщения'''
    def __init__(self, window, size=(300, 110), title='', autoclosed_time=None, text=''): 
        self.window = Toplevel(window)
        self.window.title(title)
        self.window.geometry(str(size[0])+'x'+str(size[1])+'+500+375')
        self.window.resizable(False, False)
        Label(self.window, text=text, font='Arial 10', pady=10).pack()
        Button(self.window, text='OK', width=10, height=1, 
               command = lambda: self.window.destroy()).pack()
        if autoclosed_time: 
            self.window.after(autoclosed_time, lambda: self.window.destroy())
        # пусть дочернее окно будет модальным 
        self.window.grab_set()
        self.window.focus_set()
        self.window.wait_window()
