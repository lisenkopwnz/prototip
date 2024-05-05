import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from script import *

win = tk.Tk()
win.title('Проводник')
win.geometry('500x500')
icon = PhotoImage(file = "images/png-tjpeg.jpg")
win.iconphoto(False, icon)

#def q():
    #try:
        #data = entry.get()
        #nem ='C:\\games\\' + data.split()[0].strip() +'.txt'
       # pt=Data(data,nem)
        #print(data)
    #except:
        #print('f')

def clear():
    entry.delete(0, END)

def qq():
    #os.chdir('C:\\games')
    name = entry_add.get()
    if not (f'{name}.txt') in os.getcwd():
        open(f"{name}.txt", "w")
        new_fail = f'{entry_add.get()}.txt'
        fail.append(new_fail)
        fail_set.set(fail)



    else:
        err_label["text"] = f'Файл с именем {name}.txt уже существует'





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

btn1 = ttk.Button(frame4 ,text='Отправить', command=qq)
btn1.grid(column=1, row=2)

frame2 = ttk.Frame(notebook)
frame2.pack(fill=BOTH, expand=True)

fail = ['ss']

fail_set = Variable(value=fail)

fail_listbox = Listbox(frame2, listvariable=fail_set,selectmode=SINGLE)
fail_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)



# добавляем фреймы в качестве вкладок
notebook.add(frame1, text='Записать')
notebook.add(frame2, text='Прочитать')
notebook.add(frame3, text='Ссоздать папку')

#btn1 = ttk.Button(frame1 ,text='Отправить', command=lambda: [q(), clear()])
#btn1.pack(fill = BOTH)

entry = ttk.Entry(frame1)
entry.pack(fill = BOTH)






win.mainloop()