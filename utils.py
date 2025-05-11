import pygame


class UIText:
    
    def __init__(self, name, size, text, position, color="white", background="black"):
        self.font = pygame.font.SysFont(name, size)
        self.rendered_surface = self.font.render(text, True, color, background)
        self.rect = self.rendered_surface.get_rect()
        self.rect.center = position

    def render(self, text):
        self.rendered_surface = self.font.render(text, True, "white", "black")

    def draw(self, screen):
        screen.blit(self.rendered_surface, self.rect)


class UIButton:

    def __init__(self, text, position, width, height, on_click, color="black", outline="white"):
        self.color = color
        self.position = position
        self.width = width
        self.height = height
        self.on_click = on_click
        self.outline = outline
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        if text != '':
            self.text = UIText("Arial", 20, text, [self.position.x + (self.width/2), self.position.y + (self.height/2)])

    def draw(self, screen):
    
        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.position.x-2, self.position.y-2, self.width+4, self.height+4), 0, 5)     
        pygame.draw.rect(screen, self.color, (self.position.x, self.position.y, self.width, self.height), 0, 5)
        
        if hasattr(self, "text"):
            self.text.draw(screen)


    def click(self):
        self.on_click()

    def handle_events(self, event):
        self.click()

    def mouse_is_over(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())