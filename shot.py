import pygame

from constants import *
import circleshape


class Shot(circleshape.CircleShape):
    ''

    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)

        self.forward = direction


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.forward * SHOT_SPEED * dt
        self.rect.center = self.position

    def destroy(self):
        self.kill()