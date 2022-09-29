from alura.poo.modelo.programa_tv import ProgramaTV


class Filme(ProgramaTV):
    def __init__(self, nome, ano, duracao_minutos):
        super().__init__(nome, ano)  # invocando o construtor da classe-mãe (ProgramaTV)
        self.__duracao_minutos = duracao_minutos
