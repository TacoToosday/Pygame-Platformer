# Main Python file for the platformer game
import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Platformer")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()