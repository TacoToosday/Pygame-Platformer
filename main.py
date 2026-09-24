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

# Variables and constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
GROUND_HEIGHT = 50

player_speed = 200  # pixels per second
gravity = 1200
jumpStrength = -500
verticalVelocity = 0

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


# Draw the main character
def drawMainChar(character_rect):
    pygame.draw.rect(window, (255, 0, 0), character_rect)


# Movement handling
def handle_character_movement(character_rect, speed, dt, ground_rect):
    global verticalVelocity

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        character_rect.x -= speed * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        character_rect.x += speed * dt

    # Gravity
    verticalVelocity += gravity * dt
    character_rect.y += verticalVelocity * dt

    # Stop the player if they are on the ground
    if character_rect.colliderect(ground_rect):
        character_rect.bottom = ground_rect.top
        verticalVelocity = 0

    # Keep the player inside the window bounds
    character_rect.x = max(
        0, min(character_rect.x, WINDOW_WIDTH - character_rect.width)
    )


# Main game loop
while running:
    dt = clock.tick(60) / 1000.0  # Time since last frame in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (
            event.type == pygame.KEYDOWN
            and event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP)
            and player_rect.bottom >= WINDOW_HEIGHT - GROUND_HEIGHT
        ):
            verticalVelocity = jumpStrength

    window.fill((30, 30, 30))
    ground_rect = pygame.Rect(  # The Ground
        0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, GROUND_HEIGHT
    )
    pygame.draw.rect(window, (0, 180, 0), ground_rect)
    drawMainChar(player_rect)

    handle_character_movement(player_rect, player_speed, dt, ground_rect)

    pygame.display.flip()

pygame.quit()
