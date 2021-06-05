import os
from tkinter import StringVar, Entry
from PIL import Image, ImageFont, ImageDraw
import fitz # старое название для PyMuPDF


def my_exit():
    '''Функция реализует завершение работы приложения'''
    os._exit(0)


def create_entry(frame, width_, entry_list, entry_text_list):
    '''Функция помещает в списки entry_list и entry_text_list объекты Entry и StringVar'''
    entry_text_list.append(StringVar())
    entry_list.append(Entry(frame, font = 'Arial 12', width=width_, textvariable=entry_text_list[-1])) 


def image_to_pdf(ChildWindow, main_window, entry_list, entry_text_list):
    '''Функция осуществляет чтение файла изображения и файла .pdf, 
       накладывает изображение в заданные координаты (x, y), и сохраняет в новый файл .pdf'''

    page_control = None
    image_control = None
    xywh_control = None 

    for i in range(len(entry_list)): 
        entry_list[i].get()
        
    # если указанный файл существует, записать адрес в input_pdf, иначе - None и вывести сообщение 
    if entry_text_list[0].get() == '': 
        ChildWindow(main_window, title='Об исходных данных', 
            text='Введите\nназвание файла .pdf\n', autoclosed_time=5000)
    elif not os.path.exists(os.path.join(os.getcwd(), entry_text_list[0].get())): 
        input_pdf = None 
        ChildWindow(main_window, title='Об исходных данных', 
                    text='Не получается найти\nуказанный файл .pdf\n', autoclosed_time=5000)
    else:         
        input_pdf = entry_text_list[0].get() 
        #создание файлового объекта 
        if input_pdf is not None: 
            file_object = fitz.open(os.path.join(os.getcwd(), input_pdf)) 
        else: 
            file_object = None 
        # если в файле есть указанная страница, записать её номер в n, иначе n = None    
        if entry_text_list[1].get() == '': 
            ChildWindow(main_window, title='Об исходных данных', 
                        text='Введите\nномер страницы\n', autoclosed_time=5000)
        else: 
            n = None 
            try: 
                if file_object is not None: 
                    if int(entry_text_list[1].get()) >= 1 and int(entry_text_list[1].get()) <= len(file_object): 
                        n = int(entry_text_list[1].get())
                        # если с указанием номера страницы всё в порядке - создадим объект, сожержащий эту страницу 
                        if n is not None: 
                            file_object_page_n  = file_object[n-1]
                            page_control = 'OK'
                        else: 
                            file_object_page_n = None 
                            ChildWindow(main_window, title='Об исходных данных', 
                                    text='\nНе получилось прочитать страницу\n', autoclosed_time=5000)
                    else: 
                        ChildWindow(main_window, title='Об исходных данных', 
                                    text='\nВведите n от 1 до {}\n'.format(len(file_object)), autoclosed_time=5000)
            except: 
                ChildWindow(main_window, title='Об исходных данных', 
                            text='Не получается обнаружить\nв файле указанную страницу\n', autoclosed_time=5000)
     
    # если указанный файл с изображением существует, записать адрес в input_img, иначе - None 
    if page_control == 'OK': 
        if entry_text_list[2].get() == '':
            ChildWindow(main_window, title='Об исходных данных', 
                text='Введите имя\nфайла с изображением\n', autoclosed_time=5000)
        elif not os.path.exists(os.path.join(os.getcwd(), entry_text_list[2].get())): 
            input_img = None 
            ChildWindow(main_window, title='Об исходных данных', 
                text='Не получилось прочитать\nфайл с изображением\n', autoclosed_time=5000)
        else: 
            input_img = entry_text_list[2].get() 
            try: 
                image = Image.open(os.path.join(os.getcwd(), input_img))
                image_control = 'OK'
            except: 
                input_img = None 
                ChildWindow(main_window, title='Об исходных данных', 
                            text='Не удалось прочитать\nфайл с изображением\n', autoclosed_time=5000)
        
    # если указанные значения координат и ширины/высоты адекватны, то ок, иначе pass 
    if page_control == 'OK' and image_control == 'OK': 
        try: 
            if int(entry_text_list[3].get()) >= 0: 
                x0 = int(entry_text_list[3].get())
                if int(entry_text_list[4].get()) >= 0: 
                    y0 = int(entry_text_list[4].get())
                    if int(entry_text_list[5].get()) >= 0:
                        w = int(entry_text_list[5].get()) 
                        if int(entry_text_list[6].get()) >= 0: 
                            h = int(entry_text_list[6].get())
                            x1 = x0 + w 
                            y1 = y0 + h 
                            xywh = 'OK'
                        else: 
                            ChildWindow(main_window, title='Об исходных данных', 
                                        text='Введите\положительное значение высоты\n', autoclosed_time=5000)
                    else: 
                        ChildWindow(main_window, title='Об исходных данных', 
                                    text='Введите\nоложительное значение ширины\n', autoclosed_time=5000)
                else: 
                    ChildWindow(main_window, title='Об исходных данных', 
                                text='Введите\nоложительное значение y\n', autoclosed_time=5000)            
            else: 
                ChildWindow(main_window, title='Об исходных данных', 
                            text='Введите\nоложительное значение x\n', autoclosed_time=5000)
        except: 
            xywh = None 
            ChildWindow(main_window, title='Об исходных данных', 
                        text='Не удалось\nсчитать значения\nкоординат или ширины/высоты', autoclosed_time=5000)
    
    if page_control == 'OK' and image_control == 'OK' and xywh == 'OK': 
        # если указанное имя выходного файла не содержит '?' - принять его 
        output_pdf = None  
        if entry_text_list[7].get() == '': 
            ChildWindow(main_window, title='Об исходных данных', 
                        text='Введите имя\nвыходного файла\n', autoclosed_time=5000)
        if '?' in entry_text_list[7].get(): 
            ChildWindow(main_window, title='Об исходных данных', 
                        text='Введите имя выходного файла,\nне содержащее знака "?"\n', autoclosed_time=5000)
        else: 
            output_pdf = entry_text_list[7].get()
            # вставка изображения в file_object_page_n 
            if file_object_page_n != None: 
                file_object_page_n.insertImage(fitz.Rect(x0, y0, x1, y1), 
                                               filename = os.path.join(os.getcwd(), input_img)) 
            # сохранение итогового файла 
            try: 
                file_object.save(output_pdf) 
                ChildWindow(main_window, title='О сохранении файла', 
                                text='\nФайл успешно записан\n', autoclosed_time=5000)
            except: 
                ChildWindow(main_window, title='О сохранении файла', 
                                text='\nНе удалось записать файл\n', autoclosed_time=5000)
