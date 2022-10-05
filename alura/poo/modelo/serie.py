from alura.poo.modelo.programa_tv import ProgramaTV


class Serie(ProgramaTV):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    def __str__(self):
        return f'Série "{self.nome}", lançada em {self.ano} e possui {self.__temporadas} temporada(s). ' \
               f'Possui {self.likes} like(s).'
