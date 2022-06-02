import pygame 
from pygame.sprite import Sprite
import random

class snake():
    LENGTH = 3
    COLOR = (0,0,255)
    SNAKE = [[400,400], [400,426], [400, 452]]
    
    def __init__(self):
        print('hi')
        
    def draw(self, game, screen):
        game.draw.rect(screen, self.COLOR, 3, 3)


