import pygame
import math

from constants import *
from events import *


class Menu:
    ''

    START_MENU_FLOATING_TEXT = "Press 'space' to start!"
    GAME_OVER_TEXT = "Game Over!"
    LEADERBOARD_BUTTON_TEXT = "Leaderboard"
    QUIT_BUTTON_TEXT = "Quit"

    def __init__(self):
        font = pygame.font.SysFont("Arial", 20)
        self.floating_text = font.render(self.START_MENU_FLOATING_TEXT, True, "white", "black")
        self.floating_text_rect = self.floating_text.get_rect()
        self.floating_text_rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT-(SCREEN_HEIGHT/4)]

        font = pygame.font.SysFont("Arial", 32)
        self.game_over = font.render(self.GAME_OVER_TEXT, True, "white", "black")
        self.game_over_text_rect = self.game_over.get_rect()
        self.game_over_text_rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
        

    def draw_start_menu(self, screen):
        self.draw_floating_text(screen)
        self.draw_buttons(screen)

    def draw_game_over(self, screen):
        screen.blit(self.game_over, self.game_over_text_rect)
        self.draw_floating_text(screen)
        self.draw_buttons(screen)


    def draw_floating_text(self, screen):
        t = (math.sin(pygame.time.get_ticks() / 200) + 1) / 2
        self.floating_text.set_alpha(pygame.math.lerp(80, 255, t))

        screen.blit(self.floating_text, self.floating_text_rect)

    def draw_buttons(self, screen):
        pass
