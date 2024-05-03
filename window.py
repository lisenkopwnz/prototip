import tkinter as tk
from tkinter import ttk
from tkinter import *
from script import *

win = tk.Tk()
win.title('Проводник')
win.geometry('500x500')
icon = PhotoImage(file = "images/png-tjpeg.jpg")
win.iconphoto(False, icon)

def q():
    try:
        data = entry.get()
        nem ='C:\\games\\' + data.split()[0].strip() +'.txt'
        pt=Data(data,nem)
        print(data)
    except:
        print('f')

def clear():
    entry.delete(0, END)



# Создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text='Записать')
notebook.add(frame2, text='Прочитать')

btn1 = ttk.Button(frame1 ,text='Отправить', command=lambda: [q(), clear()])
btn1.pack(fill = BOTH)

entry = ttk.Entry(frame1)
entry.pack(fill = BOTH)






win.mainloop()