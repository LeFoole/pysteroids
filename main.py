import sys
import pygame
import math

from constants import *
from events import *
from gamestatemanager import GameStateManager, GAME_STATE
from menu import Menu
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    #Pygame initialization
    pygame.init()
    pygame.display.set_caption("Pysteroids")
    #Game Variables
    GameStateManager.update_game_state(GAME_STATE.MENU)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable, drawable, asteroids, shots, menu_updatable, menu_drawable = create_and_assign_groups()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    menu = Menu()

    #Main game loop
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        match GameStateManager.GAME_STATE:
            case GAME_STATE.MENU:
                menu_updatable.update(dt)
                for obj in menu_drawable:
                    obj.draw(screen)
                draw_menu(screen, menu)

            case GAME_STATE.PLAYING:
                updatable.update(dt)
                for obj in drawable:
                    obj.draw(screen)
                detect_collisions(player, asteroids, shots)

            case GAME_STATE.OVER:
                game_over(screen, menu)

        for event in events:
            if event.type == GAME_START_EVENT:
                GameStateManager.update_game_state(GAME_STATE.PLAYING)
                asteroid_field.handle_event(event)
                player.handle_event(event)
            if event.type == GAME_OVER_EVENT:
                GameStateManager.update_game_state(GAME_STATE.OVER)
                player.handle_event(event)

        #Refresh the screen after everything was updated
        pygame.display.flip()

        #Wait for next frame time
        dt = clock.tick(60)/1000

def draw_menu(screen, menu):
    menu.draw_start_menu(screen)
                
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pygame.event.post(pygame.event.Event(GAME_START_EVENT))
        


def detect_collisions(player, asteroids, shot):
    for obj in asteroids:
        if obj.detect_collision(player):
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))
        obj.detect_collision_group(shot)



def game_over(screen, menu):
    menu.draw_game_over(screen)
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pygame.event.post(pygame.event.Event(GAME_START_EVENT))


def create_and_assign_groups():
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    menu_updatable = pygame.sprite.Group()
    menu_drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Player.shots_group = shots
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable, menu_updatable)
    AsteroidField.asteroids_group = asteroids
    Asteroid.containers = (asteroids, updatable, drawable, menu_updatable, menu_drawable)

    return updatable, drawable, asteroids, shots, menu_updatable, menu_drawable


if __name__ == "__main__":
    main()