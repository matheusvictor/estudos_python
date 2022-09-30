from alura.poo.modelo.programa_tv import ProgramaTV


class Serie(ProgramaTV):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas
