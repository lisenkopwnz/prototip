import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from script import *
from w import *

win = tk.Tk()
win.title('Проводник')
win.geometry('500x500')
icon = PhotoImage(file = "images/png-tjpeg.jpg")
win.iconphoto(False, icon)

fail = []
try:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT name_file FROM File')
    file = cursor.fetchall()
    for name_file in file:
        fail.append(name_file)
    connection.close()
except:
    print('worn')

def clear():
    selection = fail_listbox.curselection()
    print(selection)
    fail_listbox.delete(selection[0])
    selected = [fail_listbox.get(i) for i in selection]
    selected1=",".join(selected)
    print(selected1)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()



def add():
    name = entry_add.get()
    name1 = (name,)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT name_file FROM File')
    file = cursor.fetchall()
    if name1 in file:
        err_label["text"] = f'Файл с именем {name}.txt уже существует'
    else:
        cursor.execute('INSERT INTO File (name_file,data) VALUES (?,?)',
                 (name,'ddddd'))
        err_label["text"] = f'Файл с именем {name}.txt создан'
        err_label["foreground"] = 'green'
        fail_listbox.insert(0,name)

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

# Создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)

# вкладка добавить папку
frame3 = ttk.Frame(notebook)
frame3.pack(fill=BOTH, expand=True)

label = ttk.Label(frame3, text='Создать новую папку')
label.pack()

frame4 = ttk.Frame(frame3,borderwidth=1, relief=SOLID, padding=[8, 10],height = 300,width =300)
frame4.pack( anchor=NW, fill=BOTH, padx=5, pady=5)

label_name = ttk.Label(frame4, text='Введите название')
label_name.grid(column=0, row=0)

err_label = ttk.Label(frame4, foreground= 'red')
err_label.grid(column=2, row=0)

entry_add = ttk.Entry(frame4)
entry_add.grid(column=1, row=0,rowspan=2)

btn1 = ttk.Button(frame4 ,text='Отправить', command=add)
btn1.grid(column=1, row=2)

frame2 = ttk.Frame(notebook)
frame2.pack(fill=BOTH, expand=True)

fail_set = Variable(value=fail)
fail_listbox = Listbox(frame2, listvariable=fail_set,selectmode=SINGLE)
fail_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

btn1 = ttk.Button(frame2 ,text='Удалить', command=clear)
btn1.pack()



# добавляем фреймы в качестве вкладок
notebook.add(frame1, text='Записать')
notebook.add(frame2, text='Прочитать')
notebook.add(frame3, text='Ссоздать папку')



entry = ttk.Entry(frame1)
entry.pack(fill = BOTH)






win.mainloop()