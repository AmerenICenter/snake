import pygame 
from pygame.sprite import Sprite
import random

class food(Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.position = pos
        #self.game_screen = screen
        
        def draw(self):
            self.position = [random.randrange(1, 500), random.randrage(1, 500)]
            