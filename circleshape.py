import pygame


class CircleShape(pygame.sprite.Sprite):
    'Class used for collision detection between objects'

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def draw(self, screen):
        #sub-classes must override
        raise NotImplementedError


    def update(self, dt):
        #sub-classes must override
        raise NotImplementedError

    def destroy(self):
        #sub-classes must override
        raise NotImplementedError
    

    def detect_collision(self, other):
        return pygame.Vector2.distance_to(self.position, other.position) < self.radius + other.radius
    
    def detect_collision_group(self, group):
        for obj in group:
            if self.detect_collision(obj):
                obj.destroy()
                self.destroy()