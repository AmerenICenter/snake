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
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
COLOR = (255, 255, 255)

FONT = pygame.font.SysFont('Corbel', 30)
EASY = FONT.render('easy', True, COLOR)
MEDIUM = FONT.render('medium', True, COLOR)
HARD = FONT.render('hard', True, COLOR)

snake = snake()

def checkKeyPress():
    keys = pygame.key.get_pressed()
    keys[]

running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    SCREEN.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()
