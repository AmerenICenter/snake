# from transformers import WavLMModel
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
        print("Left")
        pass
    elif event.key == pygame.K_RIGHT:
        print("ROIGHT")
        pass
    elif event.key == pygame.K_UP: 
        print("UOP")
        pass 
    elif event.key == pygame.K_DOWN:
        print("DOWN")
        pass 

# def collide(head_pos, other_pos): 
    # if collide with walls
    # if collide with self
title = True
running = True
x=10
y = 10

while running:
    # if (title): 
    #     pass
    # else: 
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            checkKeyPress() 
            
    # snake.move() 
    snake_group.update()
    food_group.update()
        
    SCREEN.fill(BLACK)
    
    # for sprite in snake_group.sprites(): 
    x +=15
    y+=15
    pygame.draw.rect(SCREEN, (255,255,0), pygame.Rect(x,y,30,30))
   
    pygame.display.update()
    

pygame.quit()
