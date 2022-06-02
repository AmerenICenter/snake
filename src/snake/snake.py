import pygame 
from pygame.sprite import Sprite
import random

class snake():
    
    def __init__(self, s, dir, pos, len):
        LENGTH = 3
        COLOR = (0,0,255)
        # print('hi')
        pygame.sprite.Sprite.__init__(self)
        self.speed = s
        self.direction = dir
        self.position = pos
        self.length = len

    def move(self, pos_list, curr_pos):
        # snake_len = 3 # to change later

        # for i in range (snake_len):
            # self.position[i] += self.speed[i]
        
        pos_list.insert(0, curr_pos)

    def eat(self, pos_list, curr_pos):
        pos_list.insert(0, curr_pos)
        self.length += 1

    def draw(self, game, screen):
        game.draw.rect(screen, self.COLOR, 3, 3)

    



