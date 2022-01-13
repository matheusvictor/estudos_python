import pygame
# o pygame não é o único módulo capaz de resolver esse exercício, porém, é muito utilizado para desenvolvimento de jogos e afins.
pygame.init() # iniciando o módulo pygame
pygame.mixer.music.load('suamusica.mp3') # abre o mixer de música e carrega o arquivo importado
pygame.mixer.music.play() # comando de tocar o arquivo .mp3
# pygame.event.wait() # aguarda o áudio finalizar para encerrar o programa. Versão antiga do pygame
input('Solta o som DêJota!')