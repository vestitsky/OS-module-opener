from tkinter import *
from tkinter import filedialog as fd
import subprocess
import os
'''
1) Кнопка open file открывает окно диалога, выбераешь ярлык или программу
2) Сохраненный список файлов, показывается в отдельной колонке
3) При нажатии run открывает все сохраненные ярлыки или программы
4) Кнопка quit закрывает программу 
5) Далее создать кнопку создания и удаления категорий ярлыков
6) Выбераешь категорию и открываются те програмы, которые ты выбрал в этой категории
'''
# TODO: Сейчас это работает на тексте, сделать эту работу на файлах exe!
root = Tk()
frame = Frame(root)
text = Text(width=25, height=5, wrap=WORD)
label = Label(frame, text="Hey there.")


def insertText():  # Открыть
    file_name = fd.askopenfilename()
    text.insert(1.0, file_name)  # Путь file_name в текстовое окно
    f = open(file_name, 'rb')  # Открыть путь и прочитать
    f.close()


def extractText():  # Сохранить
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*")))
    f = open(file_name, 'w')


def buttons():  # Кнопки
    save = Button(frame, text='Run', command=extractText)
    opener = Button(frame, text='Open file', command=insertText)
    quitButton = Button(frame, text="Quit", command=frame.quit)
    save.pack()
    opener.pack()
    quitButton.pack()


def main():
    text.pack()
    label.pack()
    frame.pack()
    buttons()
    root.mainloop()


if __name__ == '__main__':
    main()




