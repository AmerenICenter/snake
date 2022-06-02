# from transformers import WavLMModel
# from torch import segment_reduce
from food import food
from snake import snake
from enum import Enum
import numpy as np

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

# def collide(head_pos, other_pos):
    # if collide with walls
    # if collide with self
title = True
running = True
size = SNAKE_WIDTH

x = SCREEN_SIZE/2
y = SCREEN_SIZE/2

init_snake_position = [[x,y], [x,y+size], [x,y+2*size]]
init_len = len(init_snake_position)
snake_obj = snake(dir = 0, pos_list = init_snake_position, length = init_len, width = size, screen = SCREEN)

food_pos = [12*random.randint(0, SCREEN_SIZE/SNAKE_WIDTH-1), 12*random.randint(0, SCREEN_SIZE/SNAKE_WIDTH-1)]

food_obj = food(pos = food_pos, screen = SCREEN, width = size)

def collide(x,y):
    print(snake_obj.pos_list)
    if x == SCREEN_SIZE or y == SCREEN_SIZE or x == -SNAKE_WIDTH or y == -SNAKE_WIDTH:
        print("Collide Wall")
        return True
    for block in snake_obj.pos_list[1:]:
        if block == snake_obj.pos_list[0]:
            print("Collide Self")
            return True
    else:
        return False

def food_collide(x, y, food_x, food_y):
    if x == food_x and y == food_y:
        print("Eat Food")
        return True
    else:
        return False

while running:
    # if (title):
    #     pass
    # else:
    pygame.time.delay(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # checkKeyPress()
            if event.key == pygame.K_LEFT:
                print("Left")
                snake_obj.direction = 2
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                snake_obj.direction = 3
            elif event.key == pygame.K_UP:
                print("UP")
                snake_obj.direction = 0
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                snake_obj.direction = 1

    # Move snake after direction change
    snake_obj.move()

    # Check for wall/snake collisions
    running = not collide(snake_obj.pos_list[0][0], snake_obj.pos_list[0][1])
    if not running:
        print("You just lost!")

    # Check for food collisions
    if food_collide(snake_obj.pos_list[0][0], snake_obj.pos_list[0][1], food_pos[0], food_pos[1]):
        snake_obj.eat()
        food_pos = [12*random.randint(0, SCREEN_SIZE/SNAKE_WIDTH-1), 12*random.randint(0, SCREEN_SIZE/SNAKE_WIDTH-1)]
        food_obj = food(pos = food_pos, screen = SCREEN, width = size)
    else:
        pass
        #print(snake_obj.pos_list[0][0], snake_obj.pos_list[0][1], food_pos[0], food_pos[1])
    # Update the screen
    SCREEN.fill(BLACK)

    # Draw snake and food
    for segment in snake_obj.pos_list:
        pygame.draw.rect(SCREEN, (255,255,0), pygame.Rect(segment[0], segment[1], SNAKE_WIDTH, SNAKE_WIDTH))
    food_obj.draw()

    # pygame.draw.rect(SCREEN, (255,255,0), pygame.Rect(x,y,SNAKE_WIDTH,SNAKE_WIDTH))

    pygame.display.update()


pygame.quit()
