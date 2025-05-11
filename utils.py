import pygame


class UIText:
    
    def __init__(self, name, size, text, position, color="white", background="black"):
        self.font = pygame.font.SysFont(name, size)
        self.rendered_surface = self.font.render(text, True, color, background)
        self.rect = self.rendered_surface.get_rect()
        self.rect.center = position

    def render(self, text):
        self.rendered_surface = self.font.render(text, True, "white", "black")