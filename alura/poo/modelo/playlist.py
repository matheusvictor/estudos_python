class Playlist(list):
    def __init__(self, nome, lista_programas):
        self.__nome = nome
        super().__init__(lista_programas)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
