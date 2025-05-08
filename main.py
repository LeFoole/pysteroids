import sys
import pygame

from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #Pygame initialization
    pygame.init()
    pygame.display.set_caption("Pysteroids")
    #Game Variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable, drawable, asteroids, shot = create_and_assign_groups()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    #Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.detect_collision(player):
                print("Game Over!")
                sys.exit()
            obj.detect_collision_group(shot)

        #Refresh the screen after everything was updated
        pygame.display.flip()

        #Wait for next frame time
        dt = clock.tick(60)/1000


def create_and_assign_groups():
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shot, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)

    return updatable, drawable, asteroids, shot


if __name__ == "__main__":
    main()