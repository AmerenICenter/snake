# from transformers import WavLMModel
from torch import segment_reduce
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
SCREEN_SIZE = 480
SCREEN = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
WIDTH = SCREEN.get_width()
HEIGHT = SCREEN.get_height()
COLOR = (255, 255, 255)
BLACK = (0,0,0)
SNAKE_WIDTH = 12

FONT = pygame.font.SysFont('Corbel', 30)
EASY = FONT.render('easy', True, COLOR)
MEDIUM = FONT.render('medium', True, COLOR)
HARD = FONT.render('hard', True, COLOR)

snake_group = pygame.sprite.Group() 
food_group = pygame.sprite.Group()



# def collide(head_pos, other_pos): 
    # if collide with walls
    # if collide with self
title = True
running = True
x_change = 12
y_change = 0
x = 200
y = 200

food_x = 12
food_y = 12

snake_x = SCREEN_SIZE/2
snake_y = SCREEN_SIZE/2

# snake = snake()

snake_blocks = []
snake_length = 1


def collide(x,y):
    if x == SCREEN_SIZE - WIDTH or y == SCREEN_SIZE - WIDTH or x == WIDTH or y == WIDTH: 
        print("Collide")
    
while running:
    # if (title): 
    #     pass
    # else: 
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # checkKeyPress() 
            if event.key == pygame.K_LEFT:
                print("Left")
                x_change = 12
                y_change = 0
                x_change = -x_change
            elif event.key == pygame.K_RIGHT:
                print("ROIGHT")
                x_change = -12
                y_change = 0 
                x_change = -x_change
            elif event.key == pygame.K_UP: 
                print("UOP")
                y_change = 12
                x_change = 0
                y_change = -y_change
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                y_change = -12
                x_change = 0
                y_change = -y_change
                
    collide(x,y)
    SCREEN.fill(BLACK)

    snake_blocks.append([snake_x, snake_y])
    if len(snake_blocks) > snake_length:
        del snake_blocks[0]
        
    for segment in snake_blocks: 
        pygame.draw.rect(SCREEN, (255,255,0), pygame.Rect(segment[0], segment[1], SNAKE_WIDTH, SNAKE_WIDTH))
    
    snake_x += x_change
    snake_y += y_change
    
    food1 = food([food_x, food_y], SCREEN)
    food1.draw()
    
    if int(snake_x) == int(food_x) & int(snake_y) == int(food_y): 
        snake_length += 1
        food_x = random.randint(1,39) * 12
        food_y = random.randint(1,39) * 12 
        print("FOOD")
        
    # x += x_change
    # y += y_change
    
    # pygame.draw.rect(SCREEN, (255,255,0), pygame.Rect(x,y,SNAKE_WIDTH,SNAKE_WIDTH))
    
    pygame.display.update()
    

pygame.quit()
