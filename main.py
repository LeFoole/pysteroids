import pygame
import sys

from constants import *
from events import *
from objectgroups import ObjectGroups
from gamestatemanager import GameStateManager, GAME_STATE
from menu import Menu
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    screen, clock = initialize_pygame() 
    dt = 0

    #Game Variables
    GameStateManager.update_game_state(GAME_STATE.MENU)

    groups = create_and_assign_groups()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    menu = Menu()

    #Main game loop
    while True:
        process_events(pygame.event.get(), player, asteroid_field)
            
        screen.fill("black")

        match GameStateManager.GAME_STATE:
            case GAME_STATE.MENU:
                groups.menu_updatable.update(dt)
                for obj in groups.menu_drawable:
                    obj.draw(screen)
                draw_menu(screen, menu)
                wait_for_start_game_input()

            case GAME_STATE.PLAYING:
                groups.updatable.update(dt)
                for obj in groups.drawable:
                    obj.draw(screen)
                detect_collisions(player, groups.asteroids, groups.shots)

            case GAME_STATE.OVER:
                draw_game_over(screen, menu)
                wait_for_start_game_input()

        #Refresh the screen after everything was updated
        pygame.display.flip()

        #Wait for next frame time
        dt = clock.tick(60)/1000


def initialize_pygame():
    #Pygame initialization
    pygame.init()
    pygame.display.set_caption("Pysteroids")

    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)), pygame.time.Clock()


def process_events(events, *event_handling_objects):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

        
        if event.type == GAME_START_EVENT:
            GameStateManager.update_game_state(GAME_STATE.PLAYING)
            #asteroid_field.handle_event(event)
            #player.handle_event(event)

        if event.type == GAME_OVER_EVENT:
            GameStateManager.update_game_state(GAME_STATE.OVER)
            #player.handle_event(event)

        if event.type != pygame.KEYDOWN:
            for obj in event_handling_objects:
                obj.handle_event(event)


def detect_collisions(player, asteroids, shots):
    detect_player_collisions(player, asteroids)
    detect_shots_collisions(shots, asteroids)

def detect_player_collisions(player, asteroids):
    hits = pygame.sprite.spritecollide(player, asteroids, dokill=False, collided=pygame.sprite.collide_circle)

    if hits:
        pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))

def detect_shots_collisions(shots, asteroids):
    hits = pygame.sprite.groupcollide(shots, asteroids, dokilla=True, dokillb=True, collided=pygame.sprite.collide_circle)

    for shot, asteroids in hits.items():
        shot.destroy()
        for asteroid in asteroids:
            asteroid.destroy()


def draw_menu(screen, menu):
    menu.draw_start_menu(screen)
        
def draw_game_over(screen, menu):
    menu.draw_game_over(screen)

def wait_for_start_game_input():
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

    return ObjectGroups(updatable, drawable, asteroids, shots, menu_updatable, menu_drawable)


if __name__ == "__main__":
    main()