import pygame

from events import *
from gamestatemanager import GameManager

class CircleShape(pygame.sprite.Sprite):
    'Class used for collision detection between objects'

    def __init__(self, x, y, radius):
        self._layer = 1
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        self.rect = pygame.Rect(0, 0, radius * 2, radius * 2)
        self.rect.center = self.position


    def draw(self, screen):
        #sub-classes must override
        raise NotImplementedError

    def update(self, dt):
        #sub-classes must override
        raise NotImplementedError

    def destroy(self):
        #sub-classes must override
        raise NotImplementedError
    

    def handle_event(self, event):
        if event.type == GAME_START_EVENT:
            self.game_start()
            return

        if event.type == GAME_OVER_EVENT:
            self.game_over()
            return