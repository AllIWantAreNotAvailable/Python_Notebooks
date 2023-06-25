from application.models.notes import SimpleNote
import os


ENCODING = 'UTF-8'
DATA_BASE_PATH = os.path.join(os.curdir, 'db')


def id_generator(path: str) -> str:
    return str(len(os.listdir(path)))


class NoteBook:

    __directory: str
    __note: SimpleNote

    def __init__(self):
        self.directory = DATA_BASE_PATH

    @property
    def directory(self):
        return self.__directory

    @directory.setter
    def directory(self, path: str):
        self.__directory = path

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: SimpleNote):
        self.__note = note

    def new(self, title: str, note: str):
        self.note = SimpleNote(id_generator(self.directory))
        self.note.title = title
        self.note.note = note

    def load(self, file_name: str):
        path = f'{os.path.join(DATA_BASE_PATH, file_name)}.json'
        with open(path, 'r', encoding=ENCODING) as note:
            self.note = SimpleNote.loads(note.read())

    def save(self):
        path = os.path.join(DATA_BASE_PATH, f'{self.note.uid} - {self.note.title}.json')
        with open(path, 'w', encoding=ENCODING) as note:
            note.write(self.note.dumps())

    def delete(self):
        path = os.path.join(DATA_BASE_PATH, f'{self.note.uid} - {self.note.title}.json')
        os.remove(path)


def tests():
    service = NoteBook()
    service.new('My note', 'My awesome note')
    print(service.note)
    service.save()
    service.load('0 - My note')
    print(service.note)
    service.delete()


if __name__ == '__main__':
    pass
else:
    tests()
