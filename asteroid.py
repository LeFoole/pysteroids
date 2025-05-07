import pygame
import random

from constants import *
import circleshape

class Asteroid(circleshape.CircleShape):
    ''

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.kind = radius / ASTEROID_MIN_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.is_out_of_bounds():
            self.kill()

    def is_out_of_bounds(self):
        return (self.position.x < -ASTEROID_MAX_RADIUS or self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS
                or self.position.y < -ASTEROID_MAX_RADIUS or self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)

    def destroy(self):
        #Subdivide if possible, kill if smallest
        if self.kind > 1:
            self.split()
        
        self.kill()

    def split(self):
            radius = ASTEROID_MIN_RADIUS * (self.kind - 1)
            direction = pygame.Vector2(0,1).rotate(random.randint(0,360))
            pos = self.position + direction
            asteroid_1 = Asteroid(pos.x + radius, pos.y, radius)
            asteroid_1.velocity = direction * random.randint(40, 100)
            asteroid_2 = Asteroid(pos.x - radius, pos.y,  radius)
            asteroid_2.velocity = -direction * random.randint(40, 100)