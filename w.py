import sqlite3


# Устанавливаем соединение с базой данных
connection = sqlite3.connect('database.db')
cursor = connection.cursor()


# Создаем таблицу File
cursor.execute('''
CREATE TABLE IF NOT EXISTS File (
id INTEGER PRIMARY KEY,
name_file TEXT NOT NULL,
data TEXT )
''')

cursor.execute('CREATE INDEX idx_name_file ON File (name_file)')


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

