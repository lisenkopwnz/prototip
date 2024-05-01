import tkinter as tk
from tkinter import ttk
from tkinter import *

win = tk.Tk()
win.title('Проводник')
win.geometry('500x500')

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









win.mainloop()