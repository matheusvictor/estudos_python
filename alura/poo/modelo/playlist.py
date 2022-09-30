class Playlist:
    def __init__(self, nome, lista_programas):
        self.nome = nome
        self.lista_programas = lista_programas

    def obter_tamanho_playlist(self):
        return len(self.lista_programas)
