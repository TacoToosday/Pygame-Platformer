# Main Python file for the platformer game
import os
import platform

import pygame

# Use a headless dummy video driver when running without a desktop display
# (for example in CI or some Linux shells). Keep normal desktop behavior intact.
if (
    platform.system() == "Linux"
    and not os.environ.get("DISPLAY")
    and not os.environ.get("WAYLAND_DISPLAY")
):
    os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

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
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800

try:  # Create the game window and handle potential errors
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
except pygame.error:
    print(
        "Unable to initialize a display. This environment may not support a graphical window."
    )
    pygame.quit()
    raise SystemExit(0)

pygame.display.set_caption("Pygame Platformer")

clock = pygame.time.Clock()

# Functions here

# Create the main character as a visible rectangle on the screen
player_rect = pygame.Rect(0, 0, 50, 50)
player_rect.center = window.get_rect().center
player_speed = 200  # pixels per second


# Draw the main character
def drawMainChar(character_rect):
    pygame.draw.rect(window, (255, 0, 0), character_rect)


# Movement handling
def handle_character_movement(character_rect, speed):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        character_rect.y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        character_rect.y += speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        character_rect.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        character_rect.x += speed

    # Keep the character inside the window bounds
    character_rect.x = max(
        0, min(character_rect.x, WINDOW_WIDTH - character_rect.width)
    )
    character_rect.y = max(
        0, min(character_rect.y, WINDOW_HEIGHT - character_rect.height)
    )


# Main game loop
while running:
    dt = clock.tick(60) / 1000.0  # Time since last frame in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_character_movement(player_rect, player_speed * dt)

    window.fill((30, 30, 30))
    drawMainChar(player_rect)

    pygame.display.flip()

pygame.quit()
