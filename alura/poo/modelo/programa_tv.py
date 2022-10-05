from abc import ABCMeta, abstractmethod


class ProgramaTV(metaclass=ABCMeta):
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.tile()

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @abstractmethod
    def __str__(self):
        return f'{self.__dict__.values()}'.strip('dict_values()')
