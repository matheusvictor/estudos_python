from alura.poo.modelo.programa_tv import ProgramaTV


class Filme(ProgramaTV):

    def __init__(self, nome, ano, duracao_minutos):
        super().__init__(nome, ano)  # invocando o construtor da classe-mãe (ProgramaTV)
        self.__duracao_minutos = duracao_minutos

    def __str__(self):
        return f'Filme "{self.nome}", lançado em {self.ano} e tem {self.__duracao_minutos} min. de duração. ' \
               f'Possui {self.likes} like(s).'
