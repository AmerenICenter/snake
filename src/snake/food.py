import pygame
from pygame.sprite import Sprite
import random

class food(Sprite):
    def __init__(self, pos, screen):
        pygame.sprite.Sprite.__init__(self)
        self.position = pos
        self.game_screen = screen

    def draw(self):
        size = 12
        # self.position = [random.randrange(0, 500-size), random.randrage(0, 500-size)]
        pygame.draw.rect(self.game_screen, (255,255,255), pygame.Rect(int(self.position[0]), int(self.position[1]), size, size))
