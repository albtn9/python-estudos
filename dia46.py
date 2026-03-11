# Dia 46 - Tocar música com pygame (requer arquivo musica.mp3 na pasta)
import pygame
pygame.init()
print('tocando')
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input()
print('Fim')
