import pygame
import random

from constants import *
import circleshape

class Asteroid(circleshape.CircleShape):
    ''

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.is_out_of_bounds():
            self.kill()

    def is_out_of_bounds(self):
        return (self.position.x < -ASTEROID_MAX_RADIUS or self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS
                or self.position.y < -ASTEROID_MAX_RADIUS or self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)
