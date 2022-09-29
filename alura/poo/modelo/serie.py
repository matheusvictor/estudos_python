class Serie:
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  # invocando o construtor da classe-mãe (ProgramaTV)
        self.__temporadas = temporadas
