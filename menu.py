import pygame
import math

from constants import *
from events import *
from utils import UIText, UIButton
from gamestatemanager import GameManager, GAME_STATE


class Menu(pygame.sprite.Sprite):
    ''

    def __init__(self):
        self._layer = 10
        super().__init__(self.containers)
        
        #self._layer = 0
        self.pre_menu_text = UIText("Arial", 20, UI_PRE_MENU_TEXT, [SCREEN_WIDTH/2, SCREEN_HEIGHT-(SCREEN_HEIGHT/4)])
        self.game_over_text = UIText("Arial", 32, UI_GAME_OVER_TEXT, [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - BUTTON_HEIGHT])
        button_x_pos = SCREEN_WIDTH/2 - BUTTON_WIDTH/2
        button_y_pos = SCREEN_HEIGHT/2 + 20
        self.start_button = UIButton("Start", pygame.Vector2(button_x_pos, button_y_pos), BUTTON_WIDTH, BUTTON_HEIGHT, self.click_start)
        button_y_pos += BUTTON_HEIGHT + 20
        self.leaderboard_button = UIButton("Leaderboard", pygame.Vector2(button_x_pos, button_y_pos), BUTTON_WIDTH, BUTTON_HEIGHT, self.click_start)
        button_y_pos += BUTTON_HEIGHT + 60
        self.quit_button = UIButton("Quit", pygame.Vector2(button_x_pos, button_y_pos), BUTTON_WIDTH, BUTTON_HEIGHT, self.click_quit)

        
    def draw(self, screen):
        match GameManager.GAME_STATE:
            case GAME_STATE.PRE_MENU:
                self.draw_pre_menu(screen)

            case GAME_STATE.MENU:
                #self.draw_pre_menu(screen)
                self.draw_menu_buttons(screen)
                pass

            case GAME_STATE.OVER:
                self.draw_game_over_text(screen)
                self.draw_menu_buttons(screen)


    def draw_game_over_text(self, screen):
        #screen.blit(self.game_over_text.rendered_surface, self.game_over_text.rect)
        #self.draw_pre_menu(screen)
        self.draw_menu_buttons(screen)
        self.game_over_text.draw(screen)


    def draw_pre_menu(self, screen):
        t = (math.sin(pygame.time.get_ticks() / 200) + 1) / 2
        self.pre_menu_text.rendered_surface.set_alpha(pygame.math.lerp(80, 255, t))

        self.pre_menu_text.draw(screen)
        #screen.blit(self.pre_menu_text.rendered_surface, self.pre_menu_text.rect)

    def draw_menu_buttons(self, screen):
        self.start_button.draw(screen)
        self.leaderboard_button.draw(screen)
        self.quit_button.draw(screen)

    def get_buttons(self):
        return (self.start_button, self.leaderboard_button, self.quit_button)

    def click_start(self):
        pygame.event.post(pygame.event.Event(GAME_START_EVENT))

    def click_quit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))