# test_pygame.py
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Test")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 150))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()