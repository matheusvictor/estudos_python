class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.tile()  # __self.nome informa que é um atributo "privado"
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter  # para ter um setter usando decorator, é preciso que antes tenha sido definido um @property (get)
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
