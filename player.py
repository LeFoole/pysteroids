import pygame

from constants import *
import circleshape

class Player(circleshape.CircleShape):
    'Player class'

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    def draw(self, screen):
        #Draw Player based on self.triangle() points
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        #Perform Player logic
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_a]:
            self.rotate(-dt)
        if pressed_keys[pygame.K_d]:
            self.rotate(dt)
        if pressed_keys[pygame.K_w]:
            self.move(dt)
        if pressed_keys[pygame.K_s]:
            self.move(-dt)
        pass

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        #Get Player direction
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def triangle(self):
        #Get the points of the triangle that represent the Player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

