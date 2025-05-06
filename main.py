import pygame

from constants import *
from player import Player

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
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        #Refresh the screen after everything was updated
        pygame.display.flip()

        #Wait for next frame time
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()