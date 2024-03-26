from sys import stdin

import Function

run = True
# Реализовать консольное приложение заметки, с сохранением,
# чтением, добавлением, редактированием и удалением заметок.

while run:
    print('Введите команду: add, edit, del, quit...')
    command = input().lower()
    match command:
        case "quit":
            print("Выход из программы...")
            run = False
        case "add":
            Function.add()
        case "edit":
            Function.edit()
        case "del":
            Function.delete()
        case _:
            print("Команда не предусмотрена...")
