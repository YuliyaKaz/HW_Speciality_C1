import Note  # Реализовать консольное приложение заметки, с сохранением,
 # чтением, добавлением, редактированием и удалением заметок.
def init():
    pass

def add():
    array = read()
    id = input("Введите номер заметки")

    not_valid_id = False
    while True:
        for notes in array:
            if notes.id == id:
                not_valid_id = True
        if not_valid_id == False:
            break
        id = input("Введите номер заметки ")
        not_valid_id = False

    head = input("Введите название заметки ")
    body = input("Введите текст заметки ")
    note = Note.Note(id, head, body)

    array.append(note)
    save(array)

def save(array):
    file = open("notes.csv", mode='w', encoding='utf8')
    for notes in array:
        file.write(Note.Note.to_string(notes) + '\n')
    file.close()
    print("Заметки сохранены...")

def read():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id=split_n[0], head=split_n[1], body=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array

def edit():
    array = read()

    id = input("Введите id заметки...")
    valid_id = False
    for notes in array:
        if notes.id == id:
            valid_id = True
            break
    if valid_id == False:
        print("Заметки с таким номером не найдено...")

    for notes in array:
        if notes.id == id:
            field = input("Какое поле хотите скорректировать? id, head, body...")
            match field:
                case "id":
                    print("Прежнее значение id = " + notes.id)
                    id = input("Введите id...")
                    notes.set_id(id)
                    break
                case "head":
                    print("Прежнее значение названия заметки = " + notes.head)
                    head = input("Введите название заметки...")
                    notes.set_head(head)
                    break
                case "body":
                    print("Прежнее значение текста заметки " + notes.body)
                    body = input("Введите текст заметки...")
                    notes.set_body(body)
                    break
                case _:
                    print("Поле не предусмотрено...")
                    break
    save(array)

def delete():
    array = read()

    id = input("Введите id заметки для удаления...")
    valid_id = False
    for notes in array:
        if notes.id == id:
            valid_id = True

    if valid_id == False:
        print("Заметки с таким номером не найдено...")
        return
    for notes in array:
        if notes.id == id:
            array.remove(notes)
            break
    save(array)


