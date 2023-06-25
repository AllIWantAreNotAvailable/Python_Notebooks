from abc import ABC


class Entity(ABC):

    __uid: str

    def __init__(self, uid: str):
        self.uid = uid

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

