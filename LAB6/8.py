import os

path = "C:/Users/TriumF/Documents\LAB6/dir_and_files/ex.txt"

if not os.path.exists(path):
    print(f"Ошибка: файл по пути '{path}' не существует")

if not os.access(path, os.W_OK):
    print(f"Ошибка: нет прав на удаление файла '{path}'")
        
os.remove(path)