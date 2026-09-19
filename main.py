# Main Python file for the platformer game
import pygame
import os

running = True
assets = os.path.join(os.path.dirname(__file__), "assets")

# Main initalization of the game (DO NOT MESS WITH THIS)
# Must be called before any other pygame functions are called
pygame.init()


# Example of loading an image from the assets folder
'''player_image = pygame.image.load(
    os.path.join(assets, "player.png")
).convert_alpha()'''

# Creation of the game window, and player
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Platformer")

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60) # Sets the FPS to 60

pygame.quit()