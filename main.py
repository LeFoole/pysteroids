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
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Shot.containers = (shot, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
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


if __name__ == "__main__":
    main()