from food import food
from snake import snake 

import random 
import pygame 

pygame.init()

# jash bare bones screen code
screen = pygame.display.set_mode([500, 500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

pygame.quit()
