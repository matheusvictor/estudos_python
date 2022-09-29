class Filme:
    def __init__(self, nome, ano, duracao_minutos):
        self.__nome = nome.tile()  # __self.nome informa que é um atributo "privado"
        self.__ano = ano
        self.__duracao = duracao_minutos
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.tile()

    @property
    def likes(self):
        """
        O decorator @property vai desempenhar o mesmo papel de um getter
        """
        return self.__likes

    def dar_likes(self):
        self.__likes += 1
