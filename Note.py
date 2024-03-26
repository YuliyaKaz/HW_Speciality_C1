import uuid
from datetime import datetime

class Note:
    def __init__(self, id=0, head="заголовок", body="заметка", date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.head = head
        self.body = body
        self.date = date

    def set_id(note, id):
        note.id = id
        note.date = date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def set_head(note, head):
        note.head = head
        note.date = date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def set_body(note, body):
        note.body = body
        note.date = date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.head + ';' + note.body + ';' + note.date
