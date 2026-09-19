# Main Python file for the platformer game
import os
import platform

# Use a headless dummy video driver when running without a desktop display
# (for example in CI or some Linux shells). Keep normal desktop behavior intact.
if platform.system() == "Linux" and not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
    os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame

running = True
assets = os.path.join(os.path.dirname(__file__), "assets")

# Main initialization of the game (DO NOT MESS WITH THIS)
# Must be called before any other pygame functions are called
pygame.init()

# Example of loading an image from the assets folder
# player_image = pygame.image.load(
#     os.path.join(assets, "player.png")
# ).convert_alpha()

# Creation of the game window, and player
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

try: # Create the game window and handle potential errors
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
except pygame.error:
    print("Unable to initialize a display. This environment may not support a graphical window.")
    pygame.quit()
    raise SystemExit(0)

pygame.display.set_caption("Pygame Platformer")

clock = pygame.time.Clock()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)  # Sets the FPS to 60

pygame.quit()