class ProgramaTV:
    def __init__(self, nome, ano):
        self.__nome = nome.tile()
        self.__ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.tile()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1
