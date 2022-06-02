from food import food
from snake import snake 

import random 
import pygame 

# jash bare bones screen code
pygame.init()
screen = pygame.display.set_mode([500, 500])
width = screen.get_width()
height = screen.get_height()
color = (255, 255, 255)

font = pygame.font.SysFont('Corbel', 30)
easy = font.render('easy', True, color)
medium = font.render('medium', True, color)
hard = font.render('hard', True, color)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

pygame.quit()
