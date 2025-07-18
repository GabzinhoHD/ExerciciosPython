#Tocando um MP3
import pygame # pygame nao é uma biblioteca nativa(deve-se instalar ele antes)
pygame.mixer.init(frequency=44100) # Define taxa de amostragem
pygame.init() # inicia a aplicação
pygame.mixer.music.load('Title-Theme.mp3') # Carrega o arquivo (A Musica é: Title Theme de Zelda: Ocarina of Time)
pygame.mixer.music.play() # Toca a musica
pygame.event.wait() # Espera a musica terminar para encerrar a aplicação
