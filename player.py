import pygame

from constants import *
import circleshape
import shot

class Player(circleshape.CircleShape):
    'Player class'

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.last_shot = 0

    def draw(self, screen):
        #Draw Player based on self.triangle() points
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        #Count weapon cooldown
        self.last_shot += dt
        
        #Perform Player logic
        self.process_input(dt, pygame.key.get_pressed())


    def process_input(self, dt, pressed_keys):
        self.process_movement_input(dt, pressed_keys)
        self.process_action_input(dt, pressed_keys)


    def process_movement_input(self, dt, pressed_keys):
        if pressed_keys[pygame.K_a]:
            self.rotate(-dt)
        if pressed_keys[pygame.K_d]:
            self.rotate(dt)
        if pressed_keys[pygame.K_w]:
            self.move(dt)
        if pressed_keys[pygame.K_s]:
            self.move(-dt)


    def process_action_input(self, dt, pressed_keys):
        if pressed_keys[pygame.K_SPACE]:
            if self.last_shot < SHOT_FIRING_RATE:
                return
            self.last_shot = 0
            shot.Shot(self.gun_point.x, self.gun_point.y, pygame.Vector2(0, 1).rotate(self.rotation))


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
        self.gun_point = a
        return [a, b, c]

    def destroy(self):
        print("Game Over!")
        #Visually explode the ship