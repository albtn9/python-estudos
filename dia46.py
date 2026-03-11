# Dia 46 - Tocar música com pygame (requer arquivo 1.mp3)
import pygame
pygame.init()
print('tocando')
pygame.mixer.music.load('Musica.mp3')
pygame.mixer.music.play()
input()
print('Fim')
