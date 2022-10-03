class Playlist:
    def __init__(self, nome, lista_programas):
        self.__nome = nome
        self.__lista_programas = lista_programas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def listagem(self):
        return self.__lista_programas

    @property
    def tamanho(self):
        return len(self.__lista_programas)
