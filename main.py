import pygame
import sys

from constants import *
from events import *
from objectgroups import ObjectGroups
from gamestatemanager import GameManager, GAME_STATE
from menu import Menu
from gameui import GameUI
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    screen, clock = initialize_pygame() 
    dt = 0

    #Game Variables
    GameManager.update_game_state(GAME_STATE.MENU)
    groups = create_and_assign_groups()
    GameManager.menu = Menu()
    GameManager.ui = GameUI()
    groups.menu_drawable.add(GameManager.menu)
    groups.drawable.add(GameManager.ui)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    #Main game loop
    while True:
        process_events(pygame.event.get(), player, asteroid_field)
            
        screen.fill("black")

        match GameManager.GAME_STATE:
            case GAME_STATE.MENU:
                groups.menu_updatable.update(dt)
                for obj in groups.menu_drawable:
                    obj.draw(screen)
                wait_for_start_game_input()

            case GAME_STATE.PLAYING:
                groups.updatable.update(dt)
                for obj in groups.drawable:
                    obj.draw(screen)
                detect_collisions(player, groups.asteroids, groups.shots)
                #ui.update(f"Score: {GameStateManager.GAME_SCORE}")

            case GAME_STATE.OVER:
                groups.menu_updatable.update(dt)
                for obj in groups.menu_drawable:
                    obj.draw(screen)
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

        if event.type == pygame.MOUSEBUTTONDOWN and GameManager.GAME_STATE != GAME_STATE.PLAYING:
            for button in GameManager.menu.get_buttons():
                if button.mouse_is_over():
                    button.handle_events(event)

        if event.type == EVENT_OPEN_MENU:
            GameManager.update_game_state(GAME_STATE.MENU)
            continue

        if event.type == SCORING_EVENT:
            event.obj.handle_event(event)
            continue
        
        if event.type == GAME_START_EVENT:
            GameManager.update_game_state(GAME_STATE.PLAYING)
            #asteroid_field.handle_event(event)
            #player.handle_event(event)

        if event.type == GAME_OVER_EVENT:
            GameManager.update_game_state(GAME_STATE.OVER)
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
            GameManager.GAME_SCORE += asteroid.radius
            pygame.event.post(pygame.event.Event(SCORING_EVENT, obj=GameManager.ui, text=f"Score: {GameManager.GAME_SCORE}"))


def wait_for_start_game_input():
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pygame.event.post(pygame.event.Event(GAME_START_EVENT))


def create_and_assign_groups():
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.LayeredUpdates()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    menu_updatable = pygame.sprite.Group()
    menu_drawable = pygame.sprite.LayeredUpdates()
    
    Player.containers = (updatable, drawable)
    Player.shots_group = shots
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable, menu_updatable)
    AsteroidField.asteroids_group = asteroids
    Asteroid.containers = (asteroids, updatable, drawable, menu_updatable, menu_drawable)
    Menu.containers = (menu_drawable)
    GameUI.containers = (drawable)

    return ObjectGroups(updatable, drawable, asteroids, shots, menu_updatable, menu_drawable)


if __name__ == "__main__":
    main()