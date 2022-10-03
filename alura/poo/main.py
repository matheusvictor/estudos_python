from alura.poo.modelo.filme import Filme
from alura.poo.modelo.serie import Serie
from alura.poo.modelo.playlist import Playlist

if __name__ == '__main__':
    filme = Filme('Transformers', 2018, 60)
    serie = Serie('narcos', 2018, 2)
    filme.nome
    print(filme.likes)
    serie.dar_likes()
    print(serie.likes)
    print(serie)

    play = Playlist('Minha playlist', [serie])
    print(play.obter_tamanho_playlist([serie]))
