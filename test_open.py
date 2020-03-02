import os
from tkinter import *
from tkinter import filedialog as fd
root = Tk()
root.geometry('400x400')
# Todo: except копии директорий
# Todo: Добавить БД для сохранения директорий или текстовый файл с сохранением их

directories = []


def open_file():
    global file_name
    file_name = fd.askopenfilename()
    directories.append(file_name)
    Label(root, text=file_name).pack()


def run():
    for starter in directories:
        os.startfile(starter)


def save():
    # Todo: Неправильная кодировка "UTF-8"
    saved = open('saved.txt', 'wt')
    saved.write(str(directories))


saved_dic_label = Label(root, text='Saved directories:').pack()
open_but = Button(root, text='Open file', command=open_file).pack()
save_but = Button(root, text='Save directories', command=save).pack()
run_but = Button(root, text='Run', command=run).pack()
exit_but = Button(root, text='Exit', command=root.quit).pack()

root.mainloop()
