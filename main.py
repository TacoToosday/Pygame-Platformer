# Main Python file for the platformer game
import os
import platform

import pygame

# Initialize Pygame, do not touch
pygame.init()

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

# Example of loading an image from the assets folder
# player_image = pygame.image.load(
#     os.path.join(assets, "player.png")
# ).convert_alpha()

# Variables and constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
GROUND_HEIGHT = 50

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

TILE_SIZE = 50
PLAYER_COLOR = (255, 0, 0)


# Main player and platform class and logic
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = 18
        self.collision_sprites = collision_sprites
        self.on_floor = False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if (
            keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]
        ) and self.on_floor:
            self.direction.y = -self.jump_speed

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        self.on_floor = False
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()


class Platform(pygame.sprite.Sprite):
    def __init__(self, rect, color, groups):
        super().__init__(*groups)
        self.image = pygame.Surface(rect.size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=rect.topleft)


all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

ground_rect = pygame.Rect(0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, GROUND_HEIGHT)
testingLevel_rect = pygame.Rect(100, WINDOW_HEIGHT - GROUND_HEIGHT - 150, 200, 50)
Platform(ground_rect, (0, 180, 0), (all_sprites, collision_sprites))
Platform(testingLevel_rect, (180, 180, 180), (all_sprites, collision_sprites))

player = Player(
    (window.get_rect().centerx, WINDOW_HEIGHT - GROUND_HEIGHT - TILE_SIZE * 2),
    all_sprites,
    collision_sprites,
)


# Main game loop
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("skyblue")
    all_sprites.update()
    all_sprites.draw(window)

    pygame.display.flip()

pygame.quit()
