#Tocando um MP3
import pygame # pygame nao é uma biblioteca nativa(deve-se instalar ele antes)
pygame.init() # iniciando
url = 'https://soundcloud.com/christian-w-154682372/01-title-theme?in=user-529993930/sets/majoras-mask-ost&si=2cd3e22179c9489e8c12dd7e82df13c9&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing' #Title Theme(Majora's Mask)
pygame.mixer.music.load(url) # Carrega o arquivo/url
pygame.mixer.music.play() # Toca a musica
pygame.event.wait() # Espera a musica terminar para encerrar a aplicação