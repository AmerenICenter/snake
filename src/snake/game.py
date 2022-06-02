from food import food
from snake import snake
from enum import Enum

import random 
import pygame 

class Direction(Enum):
    UP = 0 
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# jash bare bones screen code
pygame.init()
SCREEN = pygame.display.set_mode([500, 500])
WIDTH = SCREEN.get_width()
HEIGHT = SCREEN.get_height()
COLOR = (255, 255, 255)
BLACK = (0,0,0)

FONT = pygame.font.SysFont('Corbel', 30)
EASY = FONT.render('easy', True, COLOR)
MEDIUM = FONT.render('medium', True, COLOR)
HARD = FONT.render('hard', True, COLOR)

snake_group = pygame.sprite.Group() 
food_group = pygame.sprite.Group()

def checkKeyPress():
    if event.key == pygame.K_LEFT:
        pass
    elif event.key == pygame.K_RIGHT:
        pass
    elif event.key == pygame.K_UP: 
        pass 
    elif event.key == pygame.K_DOWN:
        pass 

title = True
running = True

while running:
    if (title): 
        pass
    else: 
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                checkKeyPress() 
                
        snake.move() 
        snake_group.update()
        food_group.update()
            
        SCREEN.fill(BLACK)
        
        pygame.display.update()

pygame.quit()
