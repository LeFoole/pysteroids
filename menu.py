import pygame
import math

from constants import *
from events import *
from utils import UIText
from gamestatemanager import GameStateManager, GAME_STATE


class Menu(pygame.sprite.Sprite):
    ''

    def __init__(self):
        super().__init__(self.containers)
        
        self.pre_menu_text = UIText("Arial", 20, UI_PRE_MENU_TEXT, [SCREEN_WIDTH/2, SCREEN_HEIGHT-(SCREEN_HEIGHT/4)])
        self.game_over_text = UIText("Arial", 32, UI_GAME_OVER_TEXT, [SCREEN_WIDTH/2, SCREEN_HEIGHT/2])

        
    def draw(self, screen):
        match GameStateManager.GAME_STATE:
            case GAME_STATE.PRE_MENU:
                self.draw_pre_menu(screen)

            case GAME_STATE.MENU:
                self.draw_pre_menu(screen)
                self.draw_menu_buttons(screen)
                pass

            case GAME_STATE.OVER:
                self.draw_game_over_text(screen)
                self.draw_menu_buttons(screen)


    def draw_start_menu(self, screen):
        self.draw_pre_menu(screen)
        self.draw_buttons(screen)

    def draw_game_over_text(self, screen):
        screen.blit(self.game_over_text.rendered_surface, self.game_over_text.rect)
        self.draw_pre_menu(screen)
        self.draw_menu_buttons(screen)


    def draw_pre_menu(self, screen):
        t = (math.sin(pygame.time.get_ticks() / 200) + 1) / 2
        self.pre_menu_text.rendered_surface.set_alpha(pygame.math.lerp(80, 255, t))

        screen.blit(self.pre_menu_text.rendered_surface, self.pre_menu_text.rect)

    def draw_menu_buttons(self, screen):
        pass