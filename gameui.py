import pygame

from events import *
from utils import UIText
from gamestatemanager import GameManager

class GameUI(pygame.sprite.Sprite):

    def __init__(self):
        self._layer = 10
        super().__init__(self.containers)
        
        self.score_text = UIText("Arial", 20, f"Score: {GameManager.GAME_SCORE}", [50, 25])

    def update(self, text):
        self.score_text.render(text)

    def draw(self, screen):
        screen.blit(self.score_text.rendered_surface, self.score_text.rect)

    def handle_event(self, event):
        if event.type == SCORING_EVENT:
            self.update(event.text)