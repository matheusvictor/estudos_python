from alura.poo.modelo.serie import Serie
from alura.poo.modelo.filme import Filme
from alura.poo.modelo.playlist import Playlist

# from alura.poo.modelo.programa_tv import ProgramaTV

if __name__ == '__main__':
    narcos = Serie('Narcos', 2015, 3)
    transformers = Filme('Transformers', 2007, 144)

    minha_playlist = Playlist('Minha playlist', [narcos, transformers])

    for programa in minha_playlist:
        print(programa)

    narcos.dar_likes()
    transformers.dar_likes()
    transformers.dar_likes()

    print(f'Tamanho da playlist: {minha_playlist.tamanho}')

    for programa in minha_playlist:
        print(programa)

    # programa = ProgramaTV('Telecurso', 2000) # impossível instanciar porque é uma classe abstrata
